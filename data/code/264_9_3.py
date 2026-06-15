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
    unique_words = find_unique_words(text)
    frequencies = count_word_frequencies(text)
    cleaned_text = remove_stop_words(text, stop_words)
    return unique_words, frequencies, cleaned_text
if __name__ == '__main__':
    sample_text = (
        "This is a sample text for word processing. "
        "This text contains some words that we want to count. "
        "Processing text involves finding unique words and removing stop words."
    )
    sample_stop_words = {"this", "is", "a", "for", "and", "some", "that", "we", "want", "to", "involves"}
    unique, frequencies, cleaned = process_text(sample_text, sample_stop_words)
    print("--- Original Text ---")
    print(sample_text)
    print("\n--- Unique Words ---")
    print(unique)
    print("\n--- Word Frequencies ---")
    print(frequencies)
    print("\n--- Cleaned Text (Stop Words Removed) ---")
    print(cleaned)