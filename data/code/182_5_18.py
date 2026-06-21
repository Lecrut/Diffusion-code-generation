def char_generator(input_string):
    for char in input_string:
        yield char

if __name__ == '__main__':
    sample_string = "Hello, World!"
    gen = char_generator(sample_string)
    for _ in range(len(sample_string)):
        print(next(gen))