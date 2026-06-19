class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    test_string = "Object-Oriented Programming in Python"
    length_of_string = analyzer.get_length(test_string)
    print(length_of_string)