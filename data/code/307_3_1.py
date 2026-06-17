def repeat_char_recursive(char, n):
    if n == 0:
        return ""
    else:
        return char + repeat_char_recursive(char, n - 1)
if __name__ == '__main__':
    char_to_repeat = 'a'
    repetitions = 5
    result = repeat_char_recursive(char_to_repeat, repetitions)
    print(result)