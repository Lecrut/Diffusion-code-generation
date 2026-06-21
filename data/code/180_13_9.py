def word_exists(word, collection):
    return word in collection

if __name__ == '__main__':
    sample_word = 'hello'
    sample_collection = {'hello', 'world', 'python', 'programming'}
    print(word_exists(sample_word, sample_collection))