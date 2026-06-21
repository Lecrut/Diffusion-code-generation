word_dict = {'apple', 'banana', 'cherry'}

def word_exists(word):
    return word in word_dict

if __name__ == '__main__':
    print(word_exists('banana'))
    print(word_exists('grape'))