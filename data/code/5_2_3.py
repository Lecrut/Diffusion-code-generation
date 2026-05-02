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
    print(comparator.compare(10, 5))
    print(comparator.compare(20, 20))
    print(comparator.compare(3, 15))
    print(comparator.compare(100, 99))