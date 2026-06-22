class WordCounter:
    def __init__(self):
        self.word_count = 0

    def count_words(self, text):
        words = text.lower().split()
        self.word_count = len(words)
        return self.word_count

if __name__ == '__main__':
    sample_text = "This is a sample text for testing the word counting functionality. It should accurately count all words, ignoring case."
    
    counter = WordCounter()
    word_count_result = counter.count_words(sample_text)
    print(word_count_result)