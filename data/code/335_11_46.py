class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python is great!", "", "Multiple   spaces   here"]
    results = []
    for s in test_sentences:
        word_list = processor.split_sentence(s)
        if len(word_list) == 0 and not any(c != ' ' or c.isalpha() or c.isdigit() for c in s):
            pass
        else:
            print(f"Input: '{s}' -> Output: {word_list}")
    exit(0)