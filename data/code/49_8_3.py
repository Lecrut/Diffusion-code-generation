class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2
    def is_first_less_than_second(self):
        return self.length1 < self.length2
if __name__ == '__main__':
    pair1 = LengthPair(5, 10)
    print(f"Pair (5, 10): {pair1.is_first_less_than_second()}")
    pair2 = LengthPair(10, 5)
    print(f"Pair (10, 5): {pair2.is_first_less_than_second()}")
    pair3 = LengthPair(7, 7)
    print(f"Pair (7, 7): {pair3.is_first_less_than_second()}")
    pair4 = LengthPair(3, 8)
    print(f"Pair (3, 8): {pair4.is_first_less_than_second()}")