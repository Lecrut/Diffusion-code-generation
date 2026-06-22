class SubsetChecker:
    def is_subset(self, set1, set2):
        return set1 <= set2

if __name__ == '__main__':
    checker = SubsetChecker()
    data1 = {1, 3, 5}
    data2 = {1, 2, 3, 4, 5}
    result = checker.is_subset(data1, data2)
    print(result)

    data3 = {6, 7, 8}
    result = checker.is_subset(data3, data2)
    print(result)