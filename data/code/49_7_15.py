class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    @classmethod
    def compare_lengths(cls, length_pair):
        return length_pair.length1 < length_pair.length2

if __name__ == '__main__':
    first_length = 30
    second_length = 60
    pair = LengthPair(first_length, second_length)
    result = LengthPair.compare_lengths(pair)
    print(result)