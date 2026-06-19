class VowelCounter:
    def __init__(self, input_string):
        self.input_string = input_string.lower()
    
    def count_vowels(self):
        vowels = set('aeiou')
        return sum(1 for char in self.input_string if char in vowels)

if __name__ == '__main__':
    sample_input = "Hello World"
    counter = VowelCounter(sample_input)
    print(counter.count_vowels())