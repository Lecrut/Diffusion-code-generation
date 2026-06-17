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
    test_cases = ["hello", "abcdefg", "aabbcc"]
    results = []
    for text in test_cases:
        has_dup = analyzer.check_for_duplicates(text)
        results.append(f"{text}: {'Yes' if has_dup else 'No'}")
    print("\n".join(results))