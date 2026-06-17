class StringProcessor:
    def find_punctuation(self, text):
        punctuation = []
        for char in text:
            if not char.isalnum():
                punctuation.append(char)
        return punctuation
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Hello, world! This is a test string with numbers 123."
    result = processor.find_punctuation(sample_string)
    print(result)