def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_text = "This is a sample sentence for testing word counting."
    if not isinstance(sample_text, str):
        raise ValueError("Input must be a string")
    
    word_count = count_words(sample_text)
    print(word_count)