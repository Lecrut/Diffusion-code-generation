def repeat_phrase(n, phrase):
    if n == 0:
        return ""
    else:
        return repeat_phrase(n - 1, phrase) + " " + phrase
if __name__ == '__main__':
    number_of_repetitions = 5
    phrase_to_repeat = "Repeat an action many times now"
    result = repeat_phrase(number_of_repetitions, phrase_to_repeat)
    print(result)