import re

class WordLengthFrequency:
    WORD_PATTERN = r'\b\w+\b'

    @staticmethod
    def count_word_lengths(text):
        words = re.findall(WordLengthFrequency.WORD_PATTERN, text)
        length_frequency = {}
        for word in words:
            length = len(word)
            if length not in length_frequency:
                length_frequency[length] = 0
            length_frequency[length] += 1
        return length_frequency

if __name__ == '__main__':
    sample_text = "Hello world! This is a test. How are you?"
    result = WordLengthFrequency.count_word_lengths(sample_text)
    print(result)