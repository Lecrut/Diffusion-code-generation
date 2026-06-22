class CharacterFrequency:
    def __init__(self):
        self.frequency = {}

    @staticmethod
    def is_valid_char(char):
        return char.isalnum() or char.isspace()

    def count_frequency(self, input_string):
        for char in input_string:
            if self.is_valid_char(char):
                if char in self.frequency:
                    self.frequency[char] += 1
                else:
                    self.frequency[char] = 1

if __name__ == '__main__':
    cf = CharacterFrequency()
    sample_string = "hello world! 123"
    cf.count_frequency(sample_string)
    print(cf.frequency)