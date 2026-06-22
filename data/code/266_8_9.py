class WordCounter:
    @staticmethod
    def count_words(text):
        return len(text.split())

if __name__ == '__main__':
    sample_text = "This is a sample text for testing the word count utility. It contains several words and punctuation marks."
    word_count = WordCounter.count_words(sample_text)
    print(word_count)