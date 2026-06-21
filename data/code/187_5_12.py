class StringAnalyzer:
    def find_largest_string_by_length(self, strings):
        return max(strings, key=len)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_strings = ["apple", "banana", "cherry", "date"]
    largest_string = analyzer.find_largest_string_by_length(sample_strings)
    print(largest_string)