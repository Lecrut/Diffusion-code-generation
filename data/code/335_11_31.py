class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python\nis\tgreat  ", "" , "Single"]
    results = []
    for s in test_sentences:
        words = processor.split_sentence(s)
        if not isinstance(words, list):
            raise TypeError("split_sentence must return a list")
        for word in words:
            if not isinstance(word, str):
                raise TypeError("All elements must be strings")
            if len(word.strip()) == 0:
                raise ValueError(f"Empty string found in result: '{word}'")
        results.append(words)
    print(results)