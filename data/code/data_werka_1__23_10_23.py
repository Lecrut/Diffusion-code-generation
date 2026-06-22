class ValueComparator:
    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            if val1 > val2:
                return ('greater', val1)
            elif val1 < val2:
                return ('less', val2)
            else:
                return ('equal', val1)
        elif isinstance(val1, str) and isinstance(val2, str):
            if val1 > val2:
                return ('greater', val1)
            elif val1 < val2:
                return ('less', val2)
            else:
                return ('equal', val1)
        else:
            raise ValueError("Both values must be either numeric or strings")

if __name__ == '__main__':
    comparator = ValueComparator()
    print(comparator.compare_values(10, 20))
    print(comparator.compare_values('apple', 'banana'))
    print(comparator.compare_values(3.5, 3.5))
    print(comparator.compare_values('cherry', 'cherry'))