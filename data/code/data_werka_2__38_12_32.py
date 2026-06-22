def has_repeated_letters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return True
        char_count[char] = 1
    return False

if __name__ == '__main__':
    sample_string = "programming"
    print(has_repeated_letters(sample_string))