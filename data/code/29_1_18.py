class VowelCounter:
    def __init__(self, text):
        self.text = text
        self.vowels = set('aeiou')

    def count(self):
        return sum(1 for char in self.text.lower() if char in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter("Rhythm is a part of life")
    print(counter.count())
    counter2 = VowelCounter("AEIOU")
    print(counter2.count())
    counter3 = VowelCounter("bcdfg")
    print(counter3.count())