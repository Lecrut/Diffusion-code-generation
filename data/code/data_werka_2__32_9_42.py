class StringAnalyzer:
    def __init__(self):
        self.text_lengths = {}

    def validate_input(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")

    def get_length(self, text):
        self.validate_input(text)
        if text in self.text_lengths:
            return self.text_lengths[text]
        else:
            length = len(text)
            self.text_lengths[text] = length
            return length

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "Hello, World!"
    sample_text2 = "Python Programming"
    print(analyzer.get_length(sample_text1))
    print(analyzer.get_length(sample_text2))
    try:
        print(analyzer.get_length(12345))
    except ValueError as e:
        print(e)