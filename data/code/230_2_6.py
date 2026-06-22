import collections

class FrequencyMapBuilder:
    @staticmethod
    def build_frequency_map(input_string):
        return collections.Counter(input_string)

if __name__ == '__main__':
    sample_string = "hello world"
    builder = FrequencyMapBuilder()
    frequency_map = builder.build_frequency_map(sample_string)
    print(frequency_map)