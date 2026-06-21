class StringAnalyzer:
    @staticmethod
    def find_longest_string(strings):
        if not strings:
            return None
        longest = ""
        for string in strings:
            if len(string) > len(longest):
                longest = string
        return longest

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(analyzer.find_longest_string(sample_strings))