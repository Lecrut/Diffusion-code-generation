class SentenceProcessor:
    def split_sentence(self, text):
        return text.split()
if __name__ == '__main__':
    processor = SentenceProcessor()
    long_text = "this is a very long sentence designed to test the efficiency of splitting algorithms on extremely long strings and ensure that the time complexity remains optimal for large inputs"
    words = processor.split_sentence(long_text)
    print(words)