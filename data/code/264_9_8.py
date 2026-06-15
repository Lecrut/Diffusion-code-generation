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
def process_text_example():
    sample_text = "The quick brown fox jumps over the lazy dog. The dog is very lazy and quick."
    stop_words = {"the", "over", "is", "and"}
    unique = find_unique_words(sample_text)
    frequencies = count_word_frequencies(sample_text)
    processed_text = remove_stop_words(sample_text, stop_words)
    print("--- Unique Words ---")
    print(unique)
    print("\n--- Word Frequencies ---")
    print(frequencies)
    print("\n--- Processed Text (Stop Words Removed) ---")
    print(processed_text)
if __name__ == '__main__':
    process_text_example()