import re

class WordFrequency:
    def __init__(self):
        self.frequency = {}

    def update_frequency(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        for word in words:
            if word in self.frequency:
                self.frequency[word] += 1
            else:
                self.frequency[word] = 1

    def get_frequency(self):
        return self.frequency

if __name__ == '__main__':
    sample_text = "Hello world! This is a test string with numbers 123 and symbols @#$."
    word_freq_instance = WordFrequency()
    word_freq_instance.update_frequency(sample_text)
    print(f"Input: '{sample_text}'")
    print(f"Output: {word_freq_instance.get_frequency()}")