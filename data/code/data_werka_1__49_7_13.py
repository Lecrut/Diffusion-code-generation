class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    @classmethod
    def is_first_less_than_second(cls, length_pair):
        return length_pair.length1 < length_pair.length2

if __name__ == '__main__':
    pair1 = LengthPair(30, 60)
    result1 = LengthPair.is_first_less_than_second(pair1)
    print(f"Is the first length less than the second for pair1? {result1}")

    pair2 = LengthPair(100, 50)
    result2 = LengthPair.is_first_less_than_second(pair2)
    print(f"Is the first length less than the second for pair2? {result2}")