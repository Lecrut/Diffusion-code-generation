def is_word_in_collection(word, collection):
    return any(word == item for item in collection)

if __name__ == '__main__':
    sample_word = 'hello'
    sample_collection = ['world', 'python', 'hello', 'code']
    print(is_word_in_collection(sample_word, sample_collection))