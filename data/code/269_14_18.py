class PunctuationIsolator:
    def __init__(self):
        self.punctuation_marks = set('.,?!:;\'\"()[]{}')

    def isolate_punctuation(self, text):
        return ''.join(sorted(filter(lambda char: char in self.punctuation_marks, text)))

if __name__ == '__main__':
    isolator = PunctuationIsolator()
    sample_string = "Hello, world! How are you? This is a test."
    result = isolator.isolate_punctuation(sample_string)
    print(result)