def check_word(word, tuple_of_strings):
    return word in tuple_of_strings

if __name__ == '__main__':
    print(check_word('hello', ('world', 'hello', 'python')))