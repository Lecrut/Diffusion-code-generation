class ValueComparator:
    def compare(self, a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare(5, 3)
    print(result1)
    result2 = comparator.compare(5, 5)
    print(result2)
    result3 = comparator.compare(2, 8)
    print(result3)