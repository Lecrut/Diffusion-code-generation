class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a > length_b:
            return f"{length_a} exceeds {length_b}"
        if length_a < length_b:
            return f"{length_a} is below {length_b}"
        return f"{length_a} matches {length_b}"

if __name__ == '__main__':
    comparator = LengthComparator()
    first_result = comparator.compare(25, 25)
    second_result = comparator.compare(100, 50)
    third_result = comparator.compare(10, 100)
    print(first_result)
    print(second_result)
    print(third_result)