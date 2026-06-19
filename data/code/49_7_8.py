class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    @classmethod
    def is_first_less_than_second(cls, length1, length2):
        return length1 < length2

if __name__ == '__main__':
    pair = LengthPair(5, 10)
    result = LengthPair.is_first_less_than_second(pair.length1, pair.length2)
    print(result)