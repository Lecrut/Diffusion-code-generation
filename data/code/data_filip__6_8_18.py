SPACE_CHAR = ' '
UNDERSCORE_CHAR = '_'

def swap_spaces_for_underscores(input_string):
    characters = list(input_string)
    for index in range(len(characters)):
        if characters[index] == SPACE_CHAR:
            characters[index] = UNDERSCORE_CHAR
    return "".join(characters)

if __name__ == '__main__':
    test_phrase = "Data Science with Python"
    converted_phrase = swap_spaces_for_underscores(test_phrase)
    print(converted_phrase)