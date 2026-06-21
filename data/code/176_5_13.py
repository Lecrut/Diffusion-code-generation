class WordGenerator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            if self.text[self.index].isspace():
                self.index += 1
            else:
                start = self.index
                while self.index < len(self.text) and not self.text[self.index].isspace():
                    self.index += 1
                return self.text[start:self.index]
        raise StopIteration

if __name__ == '__main__':
    text = "Hello, world! This is a test.  It should handle various whitespace types."
    generator = WordGenerator(text)
    for word in generator:
        print(word)