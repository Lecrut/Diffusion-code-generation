word_set = {'apple', 'banana', 'cherry'}

def word_exists(word):
    return word in word_set
if __name__ == '__main__':
    print(word_exists('banana'))
    print(word_exists('orange'))