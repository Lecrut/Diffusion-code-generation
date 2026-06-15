class TextProcessor:
    def split_alphanumeric(self, sentence):
        words = []
        for char in sentence:
            if char.isalnum():
                words.append(char)
        return words
if __name__ == '__main__':
    processor = TextProcessor()
    sample_sentence = "Hello world! This is a test sentence, 123."
    result = processor.split_alphanumeric(sample_sentence)
    print(result)