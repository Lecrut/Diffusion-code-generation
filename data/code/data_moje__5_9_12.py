class LengthComparator:
    def __init__(self, unit='m'):
        self.unit = unit

    def compare(self, length1, length2):
        if length1 > length2:
            return f"{length1} is greater than {length2}"
        elif length1 < length2:
            return f"{length1} is less than {length2}"
        else:
            return f"{length1} is equal to {length2}"

if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare(10.5, 8.2)
    print(result1)
    result2 = comparator.compare(3.0, 3.0)
    print(result2)
    result3 = comparator.compare(1.5, 4.7)
    print(result3)