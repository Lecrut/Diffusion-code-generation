def extract_distinct_words(text):
    cleaned_text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
    words = cleaned_text.split()
    return sorted(set(words))

if __name__ == '__main__':
    sample_text = "Hello world! This is a test, how are you doing today?"
    distinct_words = extract_distinct_words(sample_text)
    print(distinct_words)