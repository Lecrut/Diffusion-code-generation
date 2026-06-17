class StringAnalyzer:
    def check_for_duplicates(self, text):
        return len(set(text)) != len(text)
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    test_cases = [
        ("hello", True),
        ("abcdef", False),
        ("AaBbCc", False),
        ("aaaa", True),
    ]
    for text, expected in test_cases:
        result = analyzer.check_for_duplicates(text)
        assert result == expected, f"Failed for '{text}': got {result}, expected {expected}"
print("All tests passed.")