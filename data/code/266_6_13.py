class WordCounter:

    def count_words(self, text):
        if not text:
            return 0
        words = text.split()
        return len(words)
if __name__ == '__main__':
    counter = WordCounter()
    print(counter.count_words('Hello world'))
    print(counter.count_words('Hello   world'))
    print(counter.count_words('  Hello world  '))
    print(counter.count_words(''))