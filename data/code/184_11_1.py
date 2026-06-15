import re
from collections import Counter
class WordChecker:
    def __init__(self):
        pass
    def scan_text(self, text, keywords):
        words = re.findall(r'\b\w+\b', text.lower())
        keyword_counts = Counter()
        for word in words:
            if word in keywords:
                keyword_counts[word] += 1
        return dict(keyword_counts)
if __name__ == '__main__':
    checker = WordChecker()
    sample_text = "The quick brown fox jumps over the lazy dog. Fox and dog are friends. Quick quick quick."
    sample_keywords = ["fox", "quick", "dog", "cat"]
    report = checker.scan_text(sample_text, sample_keywords)
    print(report)