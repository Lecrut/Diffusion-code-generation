def compare_string_lengths(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else:
        return 'Equal length'
if __name__ == '__main__':
    print(compare_string_lengths('hello', 'world'))
    print(compare_string_lengths('short', 'longer string'))
    print(compare_string_lengths('same', 'same'))