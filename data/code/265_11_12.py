class CharacterFrequency:
    def __init__(self):
        self.frequency = {}

    def update_frequency(self, input_string):
        for char in input_string:
            if char.isalnum():
                if char in self.frequency:
                    self.frequency[char] += 1
                else:
                    self.frequency[char] = 1

    def get_frequency(self):
        return self.frequency

if __name__ == '__main__':
    cf = CharacterFrequency()
    test_string1 = "Hello World 123!"
    cf.update_frequency(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: {cf.get_frequency()}")

    test_string2 = "Python3.10 is great."
    cf.update_frequency(test_string2)
    print(f"Input: '{test_string2}'")
    print(f"Output: {cf.get_frequency()}")