def has_unique_characters(input_string):
    char_set = set()
    for char in input_string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

if __name__ == '__main__':
    sample_string = "abcde"
    result = has_unique_characters(sample_string)
    print(result)