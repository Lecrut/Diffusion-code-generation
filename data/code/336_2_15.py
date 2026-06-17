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
    test_cases = [
        ("hello", True),
        ("abcdefg", False),
        ("aabbccdd", True),
        ("1234567890", False)
    ]
    for text, expected in test_cases:
        result = analyzer.check_for_duplicates(text)
        assert result == expected, f"Failed for '{text}': got {result}, expected {expected}"
print("All tests passed.")