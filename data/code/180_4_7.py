def is_word_in_collection(word, collection):
    return word in collection

if __name__ == '__main__':
    sample_word = "example"
    sample_collection = ["sample", "words", "in", "collection"]
    print(is_word_in_collection(sample_word, sample_collection))