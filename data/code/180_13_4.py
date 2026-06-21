def word_exists(word, collection):
    return word in collection

if __name__ == '__main__':
    sample_word = 'apple'
    predefined_collection = {'banana', 'apple', 'cherry'}
    print(word_exists(sample_word, predefined_collection))