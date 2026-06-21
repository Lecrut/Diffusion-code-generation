def is_word_in_collection(word, collection):
    return any(word == item for item in collection)

if __name__ == '__main__':
    sample_word = 'apple'
    sample_collection = ['banana', 'cherry', 'apple', 'date']
    print(is_word_in_collection(sample_word, sample_collection))