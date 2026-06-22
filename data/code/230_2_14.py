import collections

class CharacterFrequencyBuilder:
    def build_frequency_map(self, input_string):
        return collections.Counter(input_string)

if __name__ == '__main__':
    builder = CharacterFrequencyBuilder()
    sample_string = "the quick brown fox jumps over the lazy dog"
    frequency_map = builder.build_frequency_map(sample_string)
    for char, count in frequency_map.items():
        print(f"Character: {char}, Frequency: {count}")