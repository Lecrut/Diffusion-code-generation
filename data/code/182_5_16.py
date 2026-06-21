CHAR_GENERATOR_INPUT = "Hello World"

def char_generator(input_string=CHAR_GENERATOR_INPUT):
    for char in input_string:
        yield char

if __name__ == '__main__':
    generator = char_generator()
    for char in generator:
        print(char)