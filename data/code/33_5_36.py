def non_whitespace_generator(input_string):
    for char in input_string:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    sample_input = "Python is awesome!"
    result = ''.join(non_whitespace_generator(sample_input))
    print(result)