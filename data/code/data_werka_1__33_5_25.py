def char_generator(input_string):
    for char in input_string:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    sample_string = "Hello World"
    result = ''.join(char_generator(sample_string))
    print(result)