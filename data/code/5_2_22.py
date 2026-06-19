class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a > length_b:
            return "Length A is greater than Length B"
        elif length_a < length_b:
            return "Length A is less than Length B"
        else:
            return "Length A is equal to Length B"

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.compare(10, 5))
    print(comparator.compare(3, 7))
    print(comparator.compare(8, 8))