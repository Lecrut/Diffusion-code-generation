import re

class WordFrequencyCounter:
    WORD_PATTERN = r'[a-zA-Z0-9]+'

    @staticmethod
    def extract_words(text):
        return set(re.findall(WordFrequencyCounter.WORD_PATTERN, text))

    @staticmethod
    def count_frequencies(words):
        frequency_dict = {}
        for word in words:
            if word in frequency_dict:
                frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1
        return frequency_dict

if __name__ == '__main__':
    sample_text = "Hello world! This is a test string with numbers 123 and symbols @#$."
    words = WordFrequencyCounter.extract_words(sample_text)
    frequencies = WordFrequencyCounter.count_frequencies(words)
    print(f"Input: '{sample_text}'")
    print(f"Output: {frequencies}")