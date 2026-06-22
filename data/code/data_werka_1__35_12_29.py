class VowelCounter:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def count(self, text):
        return sum(1 for char in text if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    sample_text1 = "Hello World"
    sample_text2 = "Programming is Fun"
    sample_text3 = "AEIOUaeiou"
    sample_text4 = "Rhythm"
    result1 = counter.count(sample_text1)
    result2 = counter.count(sample_text2)
    result3 = counter.count(sample_text3)
    result4 = counter.count(sample_text4)
    print(result1)
    print(result2)
    print(result3)
    print(result4)