class LengthPair:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    @classmethod
    def compare_lengths(cls, pair):
        return pair.length1 < pair.length2

if __name__ == '__main__':
    pair1 = LengthPair(30, 60)
    pair2 = LengthPair(90, 45)
    
    result1 = LengthPair.compare_lengths(pair1)
    result2 = LengthPair.compare_lengths(pair2)
    
    print(f"Is the first length of pair1 less than the second? {result1}")
    print(f"Is the first length of pair2 less than the second? {result2}")