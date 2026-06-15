def repeat_print(text, n):
    for _ in range(n):
        print(text)
if __name__ == '__main__':
    text_to_repeat = "Hello World"
    number_of_repeats = 5
    repeat_print(text_to_repeat, number_of_repeats)