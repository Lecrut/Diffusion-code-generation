class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a > length_b:
            return "length_a is greater than length_b"
        elif length_a < length_b:
            return "length_a is less than length_b"
        else:
            return "length_a is equal to length_b"

if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare(10, 5)
    result2 = comparator.compare(3, 7)
    result3 = comparator.compare(4, 4)
    print(result1)
    print(result2)
    print(result3)