from collections import Counter

class FrequencyMapBuilder:
    def build_frequency_map(self, input_string):
        return Counter(input_string)

if __name__ == '__main__':
    builder = FrequencyMapBuilder()
    sample_string = "hello world"
    frequency_map = builder.build_frequency_map(sample_string)
    print(frequency_map)