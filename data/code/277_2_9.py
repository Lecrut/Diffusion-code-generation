class VowelCounter:
    def __init__(self):
        self.vowels = "aeiouAEIOU"

    def count_vowels(self, s):
        count = 0
        for char in s:
            if char in self.vowels:
                count += 1
        return count

if __name__ == '__main__':
    counter = VowelCounter()
    sample_string = "Hello, World!"
    print(f"Number of vowels in '{sample_string}': {counter.count_vowels(sample_string)}")