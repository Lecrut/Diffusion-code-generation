def word_in_collection(word, collection):
    return word in collection

if __name__ == '__main__':
    print(word_in_collection('apple', ['banana', 'apple', 'cherry']))
    print(word_in_collection('orange', ['banana', 'apple', 'cherry']))