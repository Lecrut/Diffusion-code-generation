class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a < length_b:
            return f"{length_a} is less than {length_b}"
        elif length_a > length_b:
            return f"{length_a} is greater than {length_b}"
        else:
            return f"{length_a} equals {length_b}"

if __name__ == '__main__':
    comparator = LengthComparator()

    # Sample test cases with hard-coded values
    result1 = compare(compare, 50, 75)
    print(result1)

    result2 = compare(compare, 3.14, 2.86)
    print(result2)

    result3 = compare(compare, 100, 100)
    print(result3)