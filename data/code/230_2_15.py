import collections

class CharacterFrequencyAnalyzer:
    def __init__(self):
        self.frequency_map = {}

    def build_frequency_map(self, input_string):
        self.frequency_map = collections.Counter(input_string)

    def get_frequency_map(self):
        return self.frequency_map

if __name__ == '__main__':
    analyzer = CharacterFrequencyAnalyzer()
    sample_string = "hello world"
    analyzer.build_frequency_map(sample_string)
    frequency_map = analyzer.get_frequency_map()
    print(frequency_map)