import collections

class FrequencyMapBuilder:
    def build_frequency_map(self, input_string):
        return collections.Counter(input_string)

if __name__ == '__main__':
    builder = FrequencyMapBuilder()
    sample_string = "python programming is fun"
    frequency_map = builder.build_frequency_map(sample_string)
    print(frequency_map)