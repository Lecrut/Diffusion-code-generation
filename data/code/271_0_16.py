class CharacterFrequencyCounter:
    def __init__(self):
        self.frequency_dict = {}

    def count_characters(self, input_string):
        for char in input_string:
            if char in self.frequency_dict:
                self.frequency_dict[char] += 1
            else:
                self.frequency_dict[char] = 1

    @staticmethod
    def create_from_string(input_string):
        instance = CharacterFrequencyCounter()
        instance.count_characters(input_string)
        return instance

if __name__ == '__main__':
    sample_string = "hello world! this is a test string."
    counter = CharacterFrequencyCounter.create_from_string(sample_string)
    print(counter.frequency_dict)