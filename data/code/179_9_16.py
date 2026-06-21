def reverse_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    reversed_words = []
    for word in words:
        reversed_words.insert(0, word)
    
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(reverse_words(sample_text))