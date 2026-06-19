class CharacterFrequencyAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.frequency_map = self._build_frequency_map()

    def _build_frequency_map(self):
        frequency_map = {}
        for char in self.input_string:
            if char in frequency_map:
                frequency_map[char] += 1
            else:
                frequency_map[char] = 1
        return frequency_map

    def get_repeated_characters(self):
        repeated_chars = [char for char, count in self.frequency_map.items() if count > 1]
        return sorted(repeated_chars)

if __name__ == '__main__':
    sample_string = "character analysis"
    analyzer = CharacterFrequencyAnalyzer(sample_string)
    result = analyzer.get_repeated_characters()
    print(result)