class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    @classmethod
    def is_first_less_than_second(cls, length_pair):
        return length_pair.length1 < length_pair.length2

if __name__ == '__main__':
    LENGTH_THRESHOLD = 50
    pair1 = LengthPair(30, 60)
    pair2 = LengthPair(80, 40)

    result1 = LengthPair.is_first_less_than_second(pair1)
    result2 = LengthPair.is_first_less_than_second(pair2)

    print(f"Is the first length of pair1 less than the second? {result1}")
    print(f"Is the first length of pair2 less than the second? {result2}")