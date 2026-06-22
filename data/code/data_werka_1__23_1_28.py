class ValueComparator:

    def compare(self, val1, val2):
        if val1 > val2:
            return f'{val1} is greater than {val2}'
        elif val1 < val2:
            return f'{val1} is less than {val2}'
        else:
            return 'Both values are equal'
if __name__ == '__main__':
    comparator = ValueComparator()
    result = comparator.compare(10, 5)
    print(result)