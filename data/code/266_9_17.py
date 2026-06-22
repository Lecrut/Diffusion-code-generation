import re

class WordLengthCounter:
    WORD_PATTERN = r'\b\w+\b'

    @staticmethod
    def count_word_lengths(text):
        words = re.findall(WordLengthCounter.WORD_PATTERN, text)
        length_counts = {}
        for word in words:
            length = len(word)
            if length in length_counts:
                length_counts[length] += 1
            else:
                length_counts[length] = 1
        return length_counts

if __name__ == '__main__':
    sample_text = "Hello world! This is a test, how are you?"
    result = WordLengthCounter.count_word_lengths(sample_text)
    print(result)