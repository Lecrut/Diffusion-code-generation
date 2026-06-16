def repeat_phrase_recursive(n, phrase):
    if n == 0:
        return ""
    else:
        return phrase + repeat_phrase_recursive(n - 1, phrase)
if __name__ == '__main__':
    number_of_repeats = 5
    target_phrase = "Repeat an action many times now"
    result = repeat_phrase_recursive(number_of_repeats, target_phrase)
    print(result)