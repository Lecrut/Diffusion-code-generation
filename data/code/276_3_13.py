def repeat_characters(character, repetitions):
    return character * repetitions

if __name__ == '__main__':
    char_to_repeat = 'a'
    num_repetitions = 5
    repeated_string = repeat_characters(char_to_repeat, num_repetitions)
    print(repeated_string)