def extract_distinct_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    words = cleaned_text.split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_text = "Hello world! This is a test sentence, how are you doing today?"
    print(extract_distinct_words(sample_text))