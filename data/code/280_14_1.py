def repeat_phrase_recursive(n, phrase):
    if n == 0:
        return ""
    else:
        return phrase + repeat_phrase_recursive(n - 1, phrase)
if __name__ == '__main__':
    n_times = 5
    phrase_to_repeat = "Repeat an action many times now"
    result = repeat_phrase_recursive(n_times, phrase_to_repeat)
    print(result)