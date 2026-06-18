class StringAnalyzer:
    def check_for_duplicates(self, text):
        seen = set()
        for char in text:
            if char in seen:
                return True
            seen.add(char)
        return False
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    test_cases = ["hello", "abcdefg", "aabbc"]
    results = []
    for case in test_cases:
        result = analyzer.check_for_duplicates(case)
        results.append(f"{case}: {'Yes' if result else 'No'}")
    print("\n".join(results))