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
    samples = ["hello", "abcdefg", "aabbcc"]
    results = []
    for sample in samples:
        has_dup = analyzer.check_for_duplicates(sample)
        results.append(f"{sample}: {'has duplicates' if has_dup else 'no duplicates'}")
    print('\n'.join(results))