def are_characters_unique(input_string):
    return len(set(input_string)) == len(input_string)

if __name__ == '__main__':
    test_string = "abcdefg"
    result = are_characters_unique(test_string)
    print(result)