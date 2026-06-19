class LengthPair:
    def __init__(self, length1, length2):
        self.lengths = [length1, length2]

    @classmethod
    def is_first_less_than_second(cls, length_pair):
        return length_pair.lengths[0] < length_pair.lengths[1]

if __name__ == '__main__':
    pair = LengthPair(100, 200)
    result = LengthPair.is_first_less_than_second(pair)
    print(result)