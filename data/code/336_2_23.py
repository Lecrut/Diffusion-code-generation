class StringAnalyzer:
    def check_for_duplicates(self, text):
        seen = set()
        for char in text.lower():
            if char in seen:
                return True
            seen.add(char)
        return False
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "Hello World"
    result = analyzer.check_for_duplicates(sample_text)
    print(result)