class StringAnalyzer:
    def check_for_duplicates(self, text):
        return len(text) != len(set(text))
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    test_cases = ["hello", "abcdefg"]
    for case in test_cases:
        result = analyzer.check_for_duplicates(case)
        print(f"String '{case}' has duplicates: {result}")