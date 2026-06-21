def char_generator(input_string):
    for char in input_string:
        yield char

if __name__ == '__main__':
    generator = char_generator("Hello, World!")
    for char in generator:
        print(char)