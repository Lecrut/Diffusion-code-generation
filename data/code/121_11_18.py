class IntegerComparator:
    @staticmethod
    def compare(a, b):
        if len(a) > len(b):
            return 1
        elif len(b) > len(a):
            return -1
        else:
            for i in range(len(a)):
                if a[i] > b[i]:
                    return 1
                elif b[i] > a[i]:
                    return -1
            return 0

if __name__ == '__main__':
    comparator = IntegerComparator()
    result1 = comparator.compare([1, 2, 3], [4, 5])
    print(result1)
    result2 = comparator.compare([6, 7, 8], [9])
    print(result2)