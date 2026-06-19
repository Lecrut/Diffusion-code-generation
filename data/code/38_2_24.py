class StringAnalyzer:
    def __init__(self):
        self.seen = set()
        self.duplicates = set()

    def reset(self):
        self.seen.clear()
        self.duplicates.clear()

    def check_for_duplicates(self, input_string):
        self.reset()
        for char in input_string:
            if char in self.seen:
                self.duplicates.add(char)
            else:
                self.seen.add(char)
        return sorted(list(self.duplicates))

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_strings = [
        "hello world",
        "programming",
        "abcdefg",
        "aabbccddeeff"
    ]
    
    for sample in sample_strings:
        result = analyzer.check_for_duplicates(sample)
        print(f"Input: '{sample}', Duplicates: {result}")