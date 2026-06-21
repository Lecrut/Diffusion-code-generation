def char_generator(input_string):
    for char in input_string:
        yield char

if __name__ == '__main__':
    sample_text = "Programming is fun!"
    generator = char_generator(sample_text)
    result_list = []
    for _ in range(len(sample_text)):
        result_list.append(next(generator))
    print(result_list)