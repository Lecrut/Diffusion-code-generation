class StringAnalyzer:
    def __init__(self):
        self.length_map = {}

    def get_length(self, text):
        if text in self.length_map:
            return self.length_map[text]
        else:
            length = len(text)
            self.length_map[text] = length
            return length

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "Hello, World!"
    sample_text2 = "Python Programming"
    print(analyzer.get_length(sample_text1))
    print(analyzer.get_length(sample_text2))