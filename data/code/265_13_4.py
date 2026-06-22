class CharFrequencyAnalyzer:
    def __init__(self):
        self.char_count = {}

    def analyze(self, phrase):
        for char in phrase:
            if char in self.char_count:
                self.char_count[char] += 1
            else:
                self.char_count[char] = 1

    def get_most_frequent_chars(self):
        max_count = max(self.char_count.values())
        return [char for char, count in self.char_count.items() if count == max_count]

if __name__ == '__main__':
    analyzer = CharFrequencyAnalyzer()
    sample_phrase = "hello world"
    analyzer.analyze(sample_phrase)
    result = analyzer.get_most_frequent_chars()
    print(result)