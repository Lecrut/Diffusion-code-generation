class PunctuationIsolator:
    def __init__(self):
        self.punctuation = set(string.punctuation)

    def isolate_punctuation(self, text):
        return ''.join(char if char not in self.punctuation else ' ' for char in text)

if __name__ == '__main__':
    isolator = PunctuationIsolator()
    sample_text = "Hello, world! How are you?"
    isolated_text = isolator.isolate_punctuation(sample_text)
    print(isolated_text)