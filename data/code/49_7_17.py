class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    @staticmethod
    def compare_lengths(length_pair):
        return length_pair.length1 < length_pair.length2

if __name__ == '__main__':
    pair = LengthPair(30, 60)
    result = LengthPair.compare_lengths(pair)
    print(result)