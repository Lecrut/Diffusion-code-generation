def count_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    print(count_words(sample_text))