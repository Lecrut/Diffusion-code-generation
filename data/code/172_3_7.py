def create_word_index_mapping(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of strings")
    
    indices = sorted(range(len(words)), key=lambda x: len(words[x]))
    return {i: words[idx] for i, idx in enumerate(indices)}

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date", "elderberry"]
    word_index_dict = create_word_index_mapping(sample_words)
    print(word_index_dict)