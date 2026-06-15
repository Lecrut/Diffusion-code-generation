def char_type_generator(input_string):
    for index, char in enumerate(input_string):
        char_type = "character"
        if char.isalpha():
            char_type = "letter"
        elif char.isdigit():
            char_type = "digit"
        else:
            char_type = "symbol"
        yield (char, char_type)
if __name__ == '__main__':
    sample_string = "Hello123World!"
    generator = char_type_generator(sample_string)
    results = list(generator)
    print(results)