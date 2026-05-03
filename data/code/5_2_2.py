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
    print(comparator.compare(10, 5))
    print(comparator.compare(20, 20))
    print(comparator.compare(3, 15))
    print(comparator.compare(100, 50))