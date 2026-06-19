class LengthComparison:

    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare_lengths(self):
        try:
            if not isinstance(self.length1, (int, float)) or not isinstance(self.length2, (int, float)):
                raise ValueError('Both lengths must be numbers.')
            return self.length1 < self.length2
        except ValueError as e:
            print(f'Error: {e}')
            return None
if __name__ == '__main__':
    pair1 = LengthComparison(5.5, 10)
    print(pair1.compare_lengths())
    pair2 = LengthComparison(10, 5)
    print(pair2.compare_lengths())
    pair3 = LengthComparison(7, 7)
    print(pair3.compare_lengths())
    pair4 = LengthComparison(3, 2.8)
    print(pair4.compare_lengths())
    pair5 = LengthComparison('a', 10)
    print(pair5.compare_lengths())