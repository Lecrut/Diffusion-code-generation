class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a < length_b:
            return "Length A is shorter than Length B"
        elif length_a > length_b:
            return "Length A is longer than Length B"
        else:
            return "Length A is equal to Length B"

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.compare(5, 10))
    print(comparator.compare(15, 5))
    print(comparator.compare(10, 10))