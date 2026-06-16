class StringAnalyzer:
    def get_length(self, text):
        return len(text)
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "hello world"
    sample_text2 = ""
    sample_text3 = "Python"
    length1 = analyzer.get_length(sample_text1)
    length2 = analyzer.get_length(sample_text2)
    length3 = analyzer.get_length(sample_text3)
    print(f"Length of '{sample_text1}': {length1}")
    print(f"Length of '{sample_text2}': {length2}")
    print(f"Length of '{sample_text3}': {length3}")