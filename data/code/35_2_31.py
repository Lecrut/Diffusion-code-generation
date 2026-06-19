class VowelCounter:
    def __init__(self, input_string):
        self.input_string = input_string

    def count_vowels(self):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in self.input_string if char in vowels)

if __name__ == '__main__':
    sample_string = "Hello World"
    counter = VowelCounter(sample_string)
    print(counter.count_vowels())