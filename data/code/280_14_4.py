def repeat_phrase(n, phrase):
    if n == 0:
        return
    repeat_phrase(n - 1, phrase)
    print(phrase)
if __name__ == '__main__':
    number_of_repeats = 5
    phrase_to_print = 'Repeat an action many times now'
    repeat_phrase(number_of_repeats, phrase_to_print)