import re
from collections import Counter
def find_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)
def count_word_frequencies(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)
def remove_stop_words(text, stop_words):
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)
def process_text(text, stop_words):
    unique = find_unique_words(text)
    frequencies = count_word_frequencies(text)
    cleaned_text = remove_stop_words(text, stop_words)
    return unique, frequencies, cleaned_text
if __name__ == '__main__':
    sample_text = "This is a sample text for word processing. This text contains some words that we want to analyze. Processing is fun and useful."
    sample_stop_words = {"this", "is", "a", "for", "and", "some", "that", "we", "want"}
    unique_words, word_frequencies, cleaned_text = process_text(sample_text, sample_stop_words)
    print("--- Unique Words ---")
    print(unique_words)
    print("\n--- Word Frequencies ---")
    print(dict(word_frequencies))
    print("\n--- Cleaned Text (Stop Words Removed) ---")
    print(cleaned_text)