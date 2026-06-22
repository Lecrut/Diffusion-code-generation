def clean_text(text):
    cleaned = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    return ' '.join(cleaned.split())

def extract_distinct_words(text):
    words = clean_text(text).split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_text = "Hello world! This is a test sentence, how are you doing today?"
    result = extract_distinct_words(sample_text)
    print(result)