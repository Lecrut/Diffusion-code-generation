class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a > length_b:
            return "The first length is greater than the second length."
        elif length_a < length_b:
            return "The first length is less than the second length."
        else:
            return "The lengths are equal."

if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare(10.5, 7.2)
    print(result1)
    result2 = comparator.compare(5.0, 5.0)
    print(result2)
    result3 = comparator.compare(3.1, 9.8)
    print(result3)