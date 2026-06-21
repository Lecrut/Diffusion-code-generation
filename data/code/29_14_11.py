class VowelCounter:
    def __init__(self):
        self.vowels = frozenset("aeiouAEIOU")

    def count(self, text: str) -> int:
        count = 0
        for char in text:
            if char in self.vowels:
                count += 1
        return count

if __name__ == '__main__':
    counter = VowelCounter()
    sample_1 = "The Quick Brown Fox"
    print(counter.count(sample_1))
    sample_2 = "Rhythm Myth Gym"
    print(counter.count(sample_2))
    sample_3 = "AeiouUaei"
    print(counter.count(sample_3))