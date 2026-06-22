class VowelCounter:
    def __init__(self, text):
        self.text = text

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        return sum(1 for char in self.text if char in vowels)

if __name__ == '__main__':
    sample_string1 = "Alibaba Cloud"
    sample_string2 = "Hello, World!"
    counter1 = VowelCounter(sample_string1)
    counter2 = VowelCounter(sample_string2)
    
    print(counter1.count_vowels())
    print(counter2.count_vowels())