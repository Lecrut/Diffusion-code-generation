def all_chars_unique(char_set):
    char_count = {}
    for char in char_set:
        if char in char_count:
            return False
        char_count[char] = 1
    return True

if __name__ == '__main__':
    sample_chars = "abcdefg"
    result = all_chars_unique(sample_chars)
    print(result)

    sample_chars_with_duplicate = "hello world"
    result = all_chars_unique(sample_chars_with_duplicate)
    print(result)