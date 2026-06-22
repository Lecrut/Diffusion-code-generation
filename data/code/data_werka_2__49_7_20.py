class LengthPair:

    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def is_first_less_than_second(self):
        return self.length1 < self.length2
if __name__ == '__main__':
    pair = LengthPair(5, 10)
    result = pair.is_first_less_than_second()
    print(result)