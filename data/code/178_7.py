import re
def extract_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    return unique_words
if __name__ == '__main__':
    sample_text = "This is a sample text for word extraction. This text contains some repeated words like this and that. Sample sample."
    unique_words_set = extract_unique_words(sample_text)
    print(unique_words_set)