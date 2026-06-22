import collections

class FrequencyMap:
    @staticmethod
    def build_frequency_map(input_string):
        return collections.Counter(input_string)

if __name__ == '__main__':
    sample_string = "frequency"
    frequency_map = FrequencyMap.build_frequency_map(sample_string)
    print(frequency_map)