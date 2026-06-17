import re
from collections import Counter
class TextProcessor:
    def __init__(self, stop_words=None):
        if stop_words is None:
            self.stop_words = set()
        else:
            self.stop_words = set(word.lower() for word in stop_words)
    def find_unique_words(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        return set(words)
    def count_word_frequencies(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        return Counter(words)
    def remove_stop_words(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        filtered_words = [word for word in words if word not in self.stop_words]
        return filtered_words
if __name__ == '__main__':
    sample_text = (
        "This is a sample text for word processing. "
        "This text contains some repeated words, like this and that. "
        "We need to remove stop words such as this, is, and a. "
        "Processing text is fun."
    )
    sample_stop_words = ["this", "is", "a", "and", "for", "some"]
    processor = TextProcessor(stop_words=sample_stop_words)
    unique_words = processor.find_unique_words(sample_text)
    print("Unique Words:", unique_words)
    word_counts = processor.count_word_frequencies(sample_text)
    print("Word Frequencies:", dict(word_counts))
    filtered_words = processor.remove_stop_words(sample_text)
    print("Words after removing stop words:", filtered_words)