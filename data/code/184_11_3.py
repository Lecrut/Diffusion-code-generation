import re
from collections import Counter
class WordChecker:
    def __init__(self):
        pass
    def scan_text(self, text, keywords):
        text_lower = text.lower()
        words = re.findall(r'\b\w+\b', text_lower)
        word_counts = Counter()
        for word in words:
            if word in keywords:
                word_counts[word] += 1
        return dict(word_counts)
if __name__ == '__main__':
    checker = WordChecker()
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever and quick. Dog is very lazy."
    sample_keywords = ["fox", "quick", "dog", "cat"]
    report = checker.scan_text(sample_text, sample_keywords)
    print(report)