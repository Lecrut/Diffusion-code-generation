class StringAnalyzer:
    def check_for_duplicates(self, text):
        if not isinstance(text, str) or len(text) == 0:
            return False
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
        ("world", False),
        ("aabbccdd", True),
        ("abcdefg", False),
        ("", False)
    ]
    for text, expected in test_cases:
        result = analyzer.check_for_duplicates(text)
        assert result == expected, f"Failed for input '{text}': got {result}, expected {expected}"
print("All tests passed.")