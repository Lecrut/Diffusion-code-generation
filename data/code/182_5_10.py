def char_generator(input_string):
    yield from input_string

if __name__ == '__main__':
    test_string = "Hello World"
    generator = char_generator(test_string)
    for char in generator:
        print(char, end='')