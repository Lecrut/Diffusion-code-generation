class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2
    def compare_less_than(self):
        return self.length1 < self.length2
if __name__ == '__main__':
    pair1 = LengthPair(5, 10)
    print(pair1.compare_less_than())
    pair2 = LengthPair(10, 5)
    print(pair2.compare_less_than())
    pair3 = LengthPair(7, 7)
    print(pair3.compare_less_than())
    pair4 = LengthPair(3, 8)
    print(pair4.compare_less_than())