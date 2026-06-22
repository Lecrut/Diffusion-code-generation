class VowelCounter:
    def __init__(self):
        self.vowels = frozenset('aeiouAEIOU')

    def count(self, text):
        vowel_count = 0
        for char in text:
            if char in self.vowels:
                vowel_count += 1
        return vowel_count

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text = "Alibaba Cloud"
    print(counter.count(sample_text))