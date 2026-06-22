class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def length(self):
        return len(self.input_string)

    def is_empty(self):
        return self.length() == 0

if __name__ == '__main__':
    sample_text = "Hello, World!"
    analyzer = StringAnalyzer(sample_text)
    print(analyzer.length())
    print(analyzer.is_empty())