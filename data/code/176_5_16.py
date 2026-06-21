class WordExtractor:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            char = self.text[self.index]
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                start = self.index
                while self.index < len(self.text) and ('a' <= self.text[self.index] <= 'z' or 'A' <= self.text[self.index] <= 'Z'):
                    self.index += 1
                return self.text[start:self.index]
            else:
                self.index += 1
        raise StopIteration

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, with 123 numbers and symbols like @#$"
    extractor = WordExtractor(sample_string)
    for word in extractor:
        print(word)