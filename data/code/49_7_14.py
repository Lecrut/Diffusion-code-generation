class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    @classmethod
    def is_first_less_than_second(cls, length_pair):
        return length_pair.length1 < length_pair.length2

if __name__ == '__main__':
    LENGTH_THRESHOLD = 50
    pair = LengthPair(45, LENGTH_THRESHOLD)
    result = LengthPair.is_first_less_than_second(pair)
    print(result)