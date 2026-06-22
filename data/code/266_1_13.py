class WordCounter:
    @staticmethod
    def count_words(text):
        words = text.split()
        return len(words)

if __name__ == '__main__':
    sample_string = "This is a sample sentence for testing word counting."
    word_count = WordCounter.count_words(sample_string)
    print(word_count)