class CharacterFrequencyCounter:
    def count_characters(self, input_string):
        frequency = {}
        for char in input_string:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

if __name__ == '__main__':
    counter = CharacterFrequencyCounter()
    sample_string = "hello world"
    result = counter.count_characters(sample_string)
    print(result)