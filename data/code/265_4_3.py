def char_generator(input_string):
    for char in input_string:
        if ord(char) % 2 != 0:
            yield char
if __name__ == '__main__':
    sample_string = "aBcDeFg"
    result_generator = char_generator(sample_string)
    output_list = list(result_generator)
    print(output_list)