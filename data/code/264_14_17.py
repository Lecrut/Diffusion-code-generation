import re

def extract_words(text):
    pattern = r'\b\w+\b'
    words = re.findall(pattern, text)
    return words

def filter_and_lowercase(words):
    filtered_words = [word.lower() for word in words if word.isalpha()]
    return filtered_words

def unique_words(word_list):
    return list(set(word_list))

def tokenize_and_filter(text):
    words = extract_words(text)
    lowercase_words = filter_and_lowercase(words)
    unique_lowercased_words = unique_words(lowercase_words)
    return sorted(unique_lowercased_words)

if __name__ == '__main__':
    sample_text = "Hello World! This is a Test string with numbers 123 and symbols @#$"
    result = tokenize_and_filter(sample_text)
    print(result)