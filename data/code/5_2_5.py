class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a > length_b:
            return f"Length A ({length_a}) is greater than Length B ({length_b})"
        elif length_a < length_b:
            return f"Length A ({length_a}) is less than Length B ({length_b})"
        else:
            return f"Length A ({length_a}) is equal to Length B ({length_b})"
if __name__ == '__main__':
    comparator = LengthComparator()
    result1 = comparator.compare(10, 5)
    print(result1)
    result2 = comparator.compare(20, 20)
    print(result2)
    result3 = comparator.compare(3, 15)
    print(result3)