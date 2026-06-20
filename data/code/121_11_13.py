class IntegerComparator:
    def __init__(self, value):
        self.value = value

    def compare(self, other):
        if len(self.value) > len(other.value):
            return 1
        elif len(other.value) > len(self.value):
            return -1
        else:
            for a, b in zip(self.value, other.value):
                if a > b:
                    return 1
                elif b > a:
                    return -1
            return 0

if __name__ == '__main__':
    comparator1 = IntegerComparator([1, 2, 3, 4])
    comparator2 = IntegerComparator([5, 6])
    result1 = comparator1.compare(comparator2)
    print(result1)

    comparator3 = IntegerComparator((10, 20))
    comparator4 = IntegerComparator((30, 40, 50))
    result2 = comparator3.compare(comparator4)
    print(result2)

    comparator5 = IntegerComparator([1, 2])
    comparator6 = IntegerComparator([3, 4])
    result3 = comparator5.compare(comparator6)
    print(result3)