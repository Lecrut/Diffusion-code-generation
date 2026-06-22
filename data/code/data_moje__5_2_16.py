class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a > length_b:
            return f"{length_a} is greater than {length_b}"
        elif length_a < length_b:
            return f"{length_a} is less than {length_b}"
        else:
            return f"{length_a} is equal to {length_b}"

if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare(10, 5)
    print(result1)
    result2 = comparator.compare(3, 8)
    print(result2)
    result3 = comparator.compare(7, 7)
    print(result3)