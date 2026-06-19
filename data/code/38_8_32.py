class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.char_counts = self._count_characters()

    def _count_characters(self):
        counts = {}
        for char in self.input_string:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return counts

    def get_unique_characters(self):
        unique_chars = set()
        for char, count in self.char_counts.items():
            if count == 1:
                unique_chars.add(char)
        return unique_chars

    def get_repeated_characters(self):
        repeated_chars = []
        for char, count in self.char_counts.items():
            if count > 1:
                repeated_chars.append(char)
        return repeated_chars

if __name__ == '__main__':
    sample_string = "example"
    analyzer = StringAnalyzer(sample_string)
    unique_chars = analyzer.get_unique_characters()
    repeated_chars = analyzer.get_repeated_characters()
    print((unique_chars, repeated_chars))