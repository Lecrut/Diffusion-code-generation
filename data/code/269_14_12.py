class PunctuationIsolator:
    def __init__(self, text):
        self.text = text.lower()
    
    def isolate_punctuation(self):
        punctuation_marks = set('.,!?;:"\'()[]{}')
        return ''.join(sorted(char for char in self.text if char in punctuation_marks))

if __name__ == '__main__':
    isolator = PunctuationIsolator("Hello, world! How are you? This is a test.")
    print(isolator.isolate_punctuation())