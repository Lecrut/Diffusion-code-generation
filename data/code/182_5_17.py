def char_generator(input_string):
    for char in input_string:
        yield char

if __name__ == '__main__':
    sample_text = "Python Generator"
    generator = char_generator(sample_text)
    result_list = list(generator)
    print(result_list)