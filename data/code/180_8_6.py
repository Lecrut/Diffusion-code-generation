def is_word_in_collection(word, collection):
    if not isinstance(word, str) or not all(isinstance(item, str) for item in collection):
        raise ValueError("Both word and collection must be strings or collections of strings")
    
    return any(word == item for item in collection)

if __name__ == '__main__':
    sample_word = 'hello'
    sample_collection = ['world', 'python', 'hello', 'programming']
    print(is_word_in_collection(sample_word, sample_collection))