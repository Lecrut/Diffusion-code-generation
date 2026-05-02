class StringAnalyzer:
    def get_length(self, text):
        return len(text)
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string_1 = "hello"
    sample_string_2 = "world"
    sample_string_3 = ""
    length_1 = analyzer.get_length(sample_string_1)
    length_2 = analyzer.get_length(sample_string_2)
    length_3 = analyzer.get_length(sample_string_3)
    print(f"Length of '{sample_string_1}': {length_1}")
    print(f"Length of '{sample_string_2}': {length_2}")
    print(f"Length of '{sample_string_3}': {length_3}")