def split_string(input_string):
    return input_string.split()

if __name__ == '__main__':
    sample_string = 'Hello World from Python'
    words_list = split_string(sample_string)
    print(words_list)