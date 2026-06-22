import re

def extract_words(text):
    words = re.findall(r'\b\w+\b', text)
    return words

def remove_duplicates(words):
    unique_words = set(words)
    return list(unique_words)

def tokenize_and_filter(text):
    words = extract_words(text)
    filtered_words = remove_duplicates(words)
    return sorted(filtered_words)

if __name__ == '__main__':
    sample_text = "Hello World! This is a Test String with numbers 123 and symbols @#$."
    result = tokenize_and_filter(sample_text)
    print(result)