def is_word_in_collection(word, collection):
    return any(word == item for item in collection)

if __name__ == '__main__':
    SAMPLE_WORD = 'hello'
    SAMPLE_COLLECTION = ['world', 'python', 'hello', 'programming']
    print(is_word_in_collection(SAMPLE_WORD, SAMPLE_COLLECTION))