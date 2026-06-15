class TextProcessor:
    def split_alphanumeric(self, sentence: str) -> list[str]:
        words = []
        for char in sentence:
            if char.isalnum():
                words.append(char)
        return words
if __name__ == '__main__':
    processor = TextProcessor()
    sample_sentence = "Hello world! This is a test sentence with numbers 123."
    result = processor.split_alphanumeric(sample_sentence)
    print(result)