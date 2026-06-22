class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a > length_b:
            return f"{length_a} is longer than {length_b}"
        elif length_a < length_b:
            return f"{length_a} is shorter than {length_b}"
        else:
            return f"{length_a} is equal to {length_b}"

if __name__ == '__main__':
    comparator = LengthComparator()
    result = comparator.compare(10, 5)
    print(result)
    result2 = comparator.compare(5, 10)
    print(result2)
    result3 = comparator.compare(5, 5)
    print(result3)