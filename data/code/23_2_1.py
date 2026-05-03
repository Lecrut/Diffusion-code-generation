class ValueComparator:
    def compare(self, val1, val2):
        if val1 > val2:
            return "val1 is greater"
        elif val1 < val2:
            return "val1 is less"
        else:
            return "val1 is equal"
if __name__ == '__main__':
    comparator = ValueComparator()
    print(comparator.compare(10, 5))
    print(comparator.compare(20, 20))
    print(comparator.compare(3, 8))
    print(comparator.compare(100, 99))