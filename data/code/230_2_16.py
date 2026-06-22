import collections

class FrequencyMapBuilder:
    def validate_input(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
    
    def build_frequency_map(self, input_string):
        self.validate_input(input_string)
        return collections.Counter(input_string)

if __name__ == '__main__':
    builder = FrequencyMapBuilder()
    sample_string = "hello world"
    frequency_map = builder.build_frequency_map(sample_string)
    print(frequency_map)