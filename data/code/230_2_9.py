import collections

class FrequencyMapCreator:
    @staticmethod
    def create_frequency_map(input_string):
        return collections.Counter(input_string)

if __name__ == '__main__':
    sample_string = "example string"
    frequency_map = FrequencyMapCreator.create_frequency_map(sample_string)
    print(frequency_map)