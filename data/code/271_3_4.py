def char_type_generator(input_string):
    for index, char in enumerate(input_string):
        char_type = "letter" if 'a' <= char <= 'z' or 'A' <= char <= 'Z' else "symbol"
        yield (char, char_type)
if __name__ == '__main__':
    test_string = "Hello World123!"
    generator = char_type_generator(test_string)
    results = list(generator)
    print(results)