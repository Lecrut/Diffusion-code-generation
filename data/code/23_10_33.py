class ValueComparator:

    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            return (val1 > val2, val1 < val2, val1 == val2)
        elif isinstance(val1, str) and isinstance(val2, str):
            return (val1 > val2, val1 < val2, val1 == val2)
        else:
            raise ValueError('Both values must be either numeric or strings')
if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare_values(10, 5)
    result2 = comparator.compare_values('apple', 'banana')
    print(result1)
    print(result2)