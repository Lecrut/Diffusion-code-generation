def validate_words(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Words must be a list of strings")

def generate_word_dict():
    words = ["apple", "banana", "cherry"]
    validate_words(words)
    
    indices = sorted(range(len(words)), key=lambda i: len(words[i]))
    word_dict = {i: words[idx] for idx, i in enumerate(indices)}
    return word_dict

if __name__ == '__main__':
    print(generate_word_dict())