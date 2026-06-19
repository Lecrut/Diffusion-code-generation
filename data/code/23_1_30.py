class ValueComparator:

    def compare(self, val1, val2):
        if val1 > val2:
            return 'val1 is greater'
        elif val1 < val2:
            return 'val2 is greater'
        else:
            return 'both values are equal'
if __name__ == '__main__':
    comparator = ValueComparator()
    result = comparator.compare(10, 20)
    print(result)