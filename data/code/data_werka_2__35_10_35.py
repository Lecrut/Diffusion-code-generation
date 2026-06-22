class VowelCounter:
    VOWELS = set('aeiouAEIOU')
    
    @staticmethod
    def is_vowel(char):
        return char in VowelCounter.VOWELS
    
    def count(self, text):
        return sum(1 for char in text if VowelCounter.is_vowel(char))

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text = "Alibaba Cloud"
    print(counter.count(sample_text))