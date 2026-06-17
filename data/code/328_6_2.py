class StringAnalyzer:
    def get_length(self, text):
        return len(text)
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "hello world"
    sample_text2 = ""
    sample_text3 = "Python"
    print(f"Length of '{sample_text1}': {analyzer.get_length(sample_text1)}")
    print(f"Length of '{sample_text2}': {analyzer.get_length(sample_text2)}")
    print(f"Length of '{sample_text3}': {analyzer.get_length(sample_text3)}")