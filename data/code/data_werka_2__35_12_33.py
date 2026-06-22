class VowelCounter:
    VOWELS = set('aeiouAEIOU')

    @staticmethod
    def count_vowels(s):
        return sum(1 for char in s if char in VowelCounter.VOWELS)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud is awesome!"
    print(VowelCounter.count_vowels(sample_string))