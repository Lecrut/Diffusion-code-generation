def split_string(input_string):
    return input_string.split()

if __name__ == '__main__':
    sentence = 'Python is awesome'
    word_list = split_string(sentence)
    print(word_list)