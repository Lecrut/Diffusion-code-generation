import re

class WordFrequencyCounter:
    def __init__(self):
        self.word_count = {}

    def count_words(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def get_frequency(self, word):
        return self.word_count.get(word, 0)

if __name__ == '__main__':
    counter = WordFrequencyCounter()
    sample_text1 = "Hello world! This is a test string with numbers 123 and symbols @#."
    sample_text2 = "Programming is fun, isn't it? Python is great."

    counter.count_words(sample_text1)
    print(f"Input: '{sample_text1}'")
    print("Word Frequencies:")
    for word, freq in sorted(counter.word_count.items()):
        print(f"{word}: {freq}")

    counter.count_words(sample_text2)
    print("\nInput: 'Programming is fun, isn't it? Python is great.'")
    print("Word Frequencies:")
    for word, freq in sorted(counter.word_count.items()):
        print(f"{word}: {freq}")