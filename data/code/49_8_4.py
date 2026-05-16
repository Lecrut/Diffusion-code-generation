class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2
    def is_first_less_than_second(self):
        return self.length1 < self.length2
if __name__ == '__main__':
    pair1 = LengthPair(5, 10)
    print(f"Pair (5, 10): {pair1.is_first_less_than_second()}")
    pair2 = LengthPair(15, 15)
    print(f"Pair (15, 15): {pair2.is_first_less_than_second()}")
    pair3 = LengthPair(20, 10)
    print(f"Pair (20, 10): {pair3.is_first_less_than_second()}")
    pair4 = LengthPair(3, 3)
    print(f"Pair (3, 3): {pair4.is_first_less_than_second()}")