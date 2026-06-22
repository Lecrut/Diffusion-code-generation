class ValueComparator:

    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            if val1 > val2:
                return ('val1', 'greater')
            elif val1 < val2:
                return ('val2', 'greater')
            else:
                return ('both', 'equal')
        elif isinstance(val1, str) and isinstance(val2, str):
            if val1 > val2:
                return ('val1', 'greater')
            elif val1 < val2:
                return ('val2', 'greater')
            else:
                return ('both', 'equal')
        else:
            raise ValueError('Unsupported input types')
if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare_values(10, 5)
    print(result1)
    result2 = comparator.compare_values('apple', 'banana')
    print(result2)
    result3 = comparator.compare_values(7.5, 7.5)
    print(result3)
    result4 = comparator.compare_values('cat', 'dog')
    print(result4)