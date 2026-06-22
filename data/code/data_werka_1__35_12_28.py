class VowelCounter:
    def __init__(self):
        self.vowels_set = set("aeiouAEIOU")

    def count(self, text):
        return sum(1 for char in text if char in self.vowels_set)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text1 = "Alibaba Cloud"
    sample_text2 = "Python Programming"
    sample_text3 = "Vowels and Consonants"
    sample_text4 = "AEIOUaeiou"

    result1 = counter.count(sample_text1)
    result2 = counter.count(sample_text2)
    result3 = counter.count(sample_text3)
    result4 = counter.count(sample_text4)

    print(f"'{sample_text1}' has {result1} vowels.")
    print(f"'{sample_text2}' has {result2} vowels.")
    print(f"'{sample_text3}' has {result3} vowels.")
    print(f"'{sample_text4}' has {result4} vowels.")