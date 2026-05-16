class LengthComparator:
    def compare(self, length1, length2):
        if length1 > length2:
            return f"{length1} is greater than {length2}"
        elif length1 < length2:
            return f"{length1} is less than {length2}"
        else:
            return f"{length1} is equal to {length2}"
if __name__ == '__main__':
    comparator = LengthComparator()
    l1 = 15.5
    l2 = 20.0
    print(comparator.compare(l1, l2))
    l3 = 100
    l4 = 100
    print(comparator.compare(l3, l4))
    l5 = 5.2
    l6 = 5.20
    print(comparator.compare(l5, l6))