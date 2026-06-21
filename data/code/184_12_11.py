import re

class WordDetector:
    TARGET_PATTERN = re.compile(r'\b\w+\b', re.IGNORECASE)

    @staticmethod
    def detect_target_word(words, target):
        return any(WordDetector.TARGET_PATTERN.search(word) for word in words)

if __name__ == '__main__':
    sample_words = ["Hello", "world", "Python", "programming"]
    target_word = "python"
    result = WordDetector.detect_target_word(sample_words, target_word)
    print(result)