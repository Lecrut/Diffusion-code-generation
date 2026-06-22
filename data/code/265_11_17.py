class CharacterFrequency:
    def __init__(self):
        self.frequency = {}

    def add_character(self, char):
        if char in self.frequency:
            self.frequency[char] += 1
        else:
            self.frequency[char] = 1

    def get_frequency(self):
        return self.frequency

if __name__ == '__main__':
    cf = CharacterFrequency()
    
    test_string1 = "Hello World 123!"
    for char in test_string1:
        cf.add_character(char)
    print(cf.get_frequency())
    
    cf = CharacterFrequency()
    
    test_string2 = "Python3.10 is great."
    for char in test_string2:
        cf.add_character(char)
    print(cf.get_frequency())