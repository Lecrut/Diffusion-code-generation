def extract_distinct_words(text):
    cleaned_text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
    words = cleaned_text.split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_text = "Hello world hello Python programming is fun"
    print(extract_distinct_words(sample_text))