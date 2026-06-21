def generate_word_dict(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of strings")
    
    indices = sorted(range(len(words)), key=lambda x: len(words[x]))
    word_dict = {i: words[idx] for i, idx in enumerate(indices)}
    return word_dict

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry"]
    try:
        result_dict = generate_word_dict(sample_words)
        print(result_dict)
    except ValueError as e:
        print(e)