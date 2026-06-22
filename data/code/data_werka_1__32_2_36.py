class StringAnalyzer:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def get_length(self):
        return len(self.text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string_1 = "Hello World"
    sample_string_2 = ""
    sample_string_3 = "Python"
    analyzer.set_text(sample_string_1)
    print(f"Length of '{sample_string_1}': {analyzer.get_length()}")
    analyzer.set_text(sample_string_2)
    print(f"Length of '{sample_string_2}': {analyzer.get_length()}")
    analyzer.set_text(sample_string_3)
    print(f"Length of '{sample_string_3}': {analyzer.get_length()}")