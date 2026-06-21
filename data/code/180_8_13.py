def is_word_present(word, collection):
    return any(word == item for item in collection)

if __name__ == '__main__':
    sample_word = 'hello'
    sample_collection = ['world', 'python', 'hello', 'programming']
    print(is_word_present(sample_word, sample_collection))