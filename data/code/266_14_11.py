class WordCounter:
    @staticmethod
    def count_words(text):
        return sum(len(line.split()) for line in text.split('\n'))

if __name__ == '__main__':
    sample_text = "This is a sample text.\nIt contains multiple lines.\nEach line has words."
    counter = WordCounter()
    print(counter.count_words(sample_text))