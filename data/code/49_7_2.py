class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def is_first_less_than_second(self):
        return self.length1 < self.length2

if __name__ == '__main__':
    pair = LengthPair(3, 5)
    print(pair.is_first_less_than_second())
    pair2 = LengthPair(10, 2)
    print(pair2.is_first_less_than_second())
    pair3 = LengthPair(4, 4)
    print(pair3.is_first_less_than_second())