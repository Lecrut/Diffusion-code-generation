class WordExtractor:
    def extract_words(self, sentence):
        words = []
        for char in sentence:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                if not words or words[-1] != char.lower():
                    words.append(char)
        return words
if __name__ == '__main__':
    extractor = WordExtractor()
    sample_sentence = "Hello world! This is a test sentence, how are you doing?"
    extracted = extractor.extract_words(sample_sentence)
    print(extracted)