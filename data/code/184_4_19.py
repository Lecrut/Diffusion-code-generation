def check_word_in_tuple(word, word_tuple):
    return word in word_tuple

if __name__ == '__main__':
    print(check_word_in_tuple('hello', ('world', 'hello', 'python')))