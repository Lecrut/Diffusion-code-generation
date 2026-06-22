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
    print(comparator.compare_values(10, 5))
    print(comparator.compare_values('apple', 'banana'))
    print(comparator.compare_values(7.5, 7.5))