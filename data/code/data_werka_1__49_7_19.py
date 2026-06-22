class LengthPair:
    def __init__(self, length1, length2):
        self.lengths = {'first': length1, 'second': length2}

    @classmethod
    def is_first_less_than_second(cls, length_pair):
        return length_pair.lengths['first'] < length_pair.lengths['second']

if __name__ == '__main__':
    pair = LengthPair(90, 45)
    result = LengthPair.is_first_less_than_second(pair)
    print(result)