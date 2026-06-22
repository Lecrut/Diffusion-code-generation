def count_unique_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

if __name__ == '__main__':
    sample_text = "hello world hello Python"
    print(count_unique_words(sample_text))