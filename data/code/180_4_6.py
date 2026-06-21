def word_in_collection(word, collection):
    return word in collection

if __name__ == '__main__':
    sample_word = 'apple'
    sample_collection = ['banana', 'apple', 'cherry']
    print(word_in_collection(sample_word, sample_collection))