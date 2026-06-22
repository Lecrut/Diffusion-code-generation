class PunctuationReplacer:
    def __init__(self):
        self.punctuation_marks = '.,!?;:'

    def replace_punctuation(self, text):
        return ''.join(' ' if char in self.punctuation_marks else char for char in text)

if __name__ == '__main__':
    replacer = PunctuationReplacer()
    sample_string = "Hello world! How are you, today? Let's check: 123."
    result = replacer.replace_punctuation(sample_string)
    print(result)