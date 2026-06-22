class VowelCounter:
    VOWELS = set('aeiouAEIOU')
    
    def count(self, text):
        return sum(1 for char in text if char in self.VOWELS)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text = "Alibaba Cloud is an innovative technology company."
    print(counter.count(sample_text))