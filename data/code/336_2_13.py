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
    sample_text = "hello"
    result = analyzer.check_for_duplicates(sample_text)
    print(f"Duplicates found in '{sample_text}': {result}")