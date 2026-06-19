class LengthComparison:

    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        try:
            if not isinstance(self.length1, (int, float)) or not isinstance(self.length2, (int, float)):
                raise ValueError('Both lengths must be numbers.')
            return self.length1 < self.length2
        except ValueError as e:
            print(f'Error: {e}')
            return None
if __name__ == '__main__':
    comparison1 = LengthComparison(3.5, 4.2)
    result1 = comparison1.compare()
    if result1 is not None:
        print(result1)
    comparison2 = LengthComparison(8, 5)
    result2 = comparison2.compare()
    if result2 is not None:
        print(result2)
    comparison3 = LengthComparison(7, 7)
    result3 = comparison3.compare()
    if result3 is not None:
        print(result3)
    comparison4 = LengthComparison('10', 5)
    result4 = comparison4.compare()
    if result4 is not None:
        print(result4)