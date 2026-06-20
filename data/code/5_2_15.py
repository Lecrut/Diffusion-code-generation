class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a > length_b:
            return "Length A is longer than Length B."
        elif length_b > length_a:
            return "Length B is longer than Length A."
        else:
            return "Lengths are equal."

if __name__ == '__main__':
    comparator = LengthComparator()
    result = comparator.compare(10, 5)
    print(result)