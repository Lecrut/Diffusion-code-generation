def generate_word_dict(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the list must be strings")
    
    indices = sorted(range(len(words)), key=lambda x: len(words[x]))
    word_dict = {i: words[idx] for i, idx in enumerate(indices)}
    return word_dict

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry"]
    result_dict = generate_word_dict(sample_words)
    print(result_dict)