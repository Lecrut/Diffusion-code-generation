class VowelCounter:
    def __init__(self, text):
        self.text = text
    
    def is_vowel(self, char):
        vowels = "aeiouAEIOU"
        return char in vowels
    
    def count_vowels(self):
        count = 0
        for char in self.text:
            if self.is_vowel(char):
                count += 1
        return count

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    counter = VowelCounter(sample_string)
    vowel_count = counter.count_vowels()
    print(vowel_count)