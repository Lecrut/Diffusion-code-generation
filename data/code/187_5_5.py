class StringAnalyzer:
    def __init__(self, strings):
        self.strings = strings

    def find_largest_string_by_length(self):
        return max(self.strings, key=len)

if __name__ == '__main__':
    analyzer = StringAnalyzer(["apple", "banana", "cherry", "date"])
    largest_string = analyzer.find_largest_string_by_length()
    print(largest_string)