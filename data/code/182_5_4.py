def char_generator(input_string):
    for char in input_string:
        yield char

if __name__ == '__main__':
    gen = char_generator("Hello, World!")
    for _ in range(5):
        print(next(gen))