class StringAnalyzer:
    @staticmethod
    def find_longest_string(string_list):
        if not string_list:
            return None
        longest_string = max(string_list, key=len)
        return longest_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    analyzer = StringAnalyzer()
    result = analyzer.find_longest_string(sample_strings)
    print(result)