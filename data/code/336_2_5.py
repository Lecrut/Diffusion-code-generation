class StringAnalyzer:
    def check_for_duplicates(self, text):
        return len(set(text)) != len(text)
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "hello"
    has_dupes = analyzer.check_for_duplicates(sample_text)
    print("Duplicates found:", has_dupes)