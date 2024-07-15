from tkinter import *
# from pandas import *
from json import *
from random import choice
# from time import sleep
BACKGROUND_COLOR = "#B1DDC6"
status = "front"
word_generated = ''

# ---------------------x defining all necessary function x----------------------x


def delete_label(label):
    label.destroy()


def right():
    global status
    global word_generated
    meaning_label.destroy()
    if status == 'back':
        with open("data/french words list.txt") as french_words_file:
            list = french_words_file.readlines()
            for i in range(len(list) - 1):
                list[i] = list[i].strip()
            list.remove(word_generated)
        with open("data/french words list.txt", mode='w') as french_words_file:
            french_words_file.writelines(f"{element}\n" for element in list)
        # remove those key value pair from the json file as well
        show_front()


def wrong():
    global status
    meaning_label.destroy()
    if status == 'back':
        show_front()


def show_front():
    global status
    global word_generated
    status = 'front'
    with open("data/french words list.txt", mode='r') as french_words_file:
        list = french_words_file.readlines()
        for i in range(len(list)-1):
            list[i] = list[i].strip()
    word_generated = choice(list)
    front_canvas.grid(row=0, column=0, columnspan=2)
    language_label = Label(text="French", font=("Ariel", 40, "italic"))
    front_canvas.create_window(400, 150, window=language_label)
    word_label = Label(text=word_generated, font=("Ariel", 60, "bold"))
    front_canvas.create_window(400, 263, window=word_label)
    screen.after(3000, show_back)
    screen.after(3000, lambda: delete_label(word_label))



def show_back():
    global status
    global word_generated
    global meaning_label
    status = 'back'
    with open("data/French words.json", mode='r') as dictionary_file:
        dictionary = load(dictionary_file)
        word_meaning = dictionary[word_generated]
    meaning_label = Label(text=word_meaning, font=("Ariel", 90, "bold"))
    front_canvas.grid_forget()
    back_canvas.grid(row=0, column=0, columnspan=2)
    back_canvas.create_window(400, 263, window=meaning_label)


# # creating a json file and a words list containing all the words and necessary information
# words_data_frame = read_csv("data/French words - Sheet1.csv")
# french_words_list = []
# for (index, row) in words_data_frame.iterrows():
#     actual_word = row["French word"]
#     with open("data/French words list.txt", mode='a') as words_list_file:
#         words_list_file.write(f"{actual_word}\n")
#
#     french_words_list.append(actual_word)
#     meaning = row["Meaning"]
#     new_data = {actual_word: meaning}
#     try:
#         with open("data/French words.json", mode='r') as words_dictionary:
#             old_dictionary = load(words_dictionary)
#             old_dictionary.update(new_data)
#         with open("data/French words.json", mode='w') as words_dictionary:
#             dump(old_dictionary, words_dictionary, indent=4)
#     except JSONDecodeError:
#         with open("data/French words.json", mode='w') as words_dictionary:
#             dump(new_data, words_dictionary, indent=4)
#

# creating the main window
screen = Tk()
screen.title("Flashy learner")
screen.config(bg=BACKGROUND_COLOR)
screen.config(padx=50, pady=50)

# creating front side canvas
front_canvas = Canvas(width=800, height=526)
card_front_photo_image = PhotoImage(file="images/card_front.png")
front_canvas.create_image(400, 263, image=card_front_photo_image)

# front_canvas.pack()

# creating back side canvas
back_canvas = Canvas(width=800, height=526)
card_back_photo_image = PhotoImage(file="images/card_back.png")
back_canvas.create_image(400, 263, image=card_back_photo_image)
# back_canvas.grid(row=0, column=0, columnspan=2)

# creating right and wrong buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_button.grid(row=1, column=1)

show_front()

mainloop()
