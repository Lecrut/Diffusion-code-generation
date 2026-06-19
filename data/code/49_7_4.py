class LengthPair:

    def __init__(self, length1, length2):
        if not (isinstance(length1, (int, float)) and isinstance(length2, (int, float))):
            raise ValueError('Both lengths must be numbers.')
        self.length1 = length1
        self.length2 = length2

    @classmethod
    def is_first_less_than_second(cls, length_pair):
        return length_pair.length1 < length_pair.length2
if __name__ == '__main__':
    try:
        pair = LengthPair(30.5, 40.2)
        result = LengthPair.is_first_less_than_second(pair)
        print(result)
    except ValueError as e:
        print(e)