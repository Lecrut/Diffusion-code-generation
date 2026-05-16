class VowelCounter:
    def __init__(self, text):
        self.text = text
    def count_vowels(self):
        vowels = "aeiouAEIOU"
        count = 0
        for char in self.text:
            if char in vowels:
                count += 1
        return count
if __name__ == '__main__':
    sample_string = "Hello World"
    counter = VowelCounter(sample_string)
    vowel_count = counter.count_vowels()
    print(vowel_count)