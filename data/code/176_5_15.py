def is_whitespace(char):
    return char.isspace()

class WordGenerator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text) and is_whitespace(self.text[self.index]):
            self.index += 1
        
        if self.index >= len(self.text):
            raise StopIteration

        start = self.index
        while self.index < len(self.text) and not is_whitespace(self.text[self.index]):
            self.index += 1
        
        return self.text[start:self.index]

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, with 123 numbers and symbols like @#$"
    generator = WordGenerator(sample_string)
    for word in generator:
        print(word)