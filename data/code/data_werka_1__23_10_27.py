class ValueComparator:
    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            if val1 > val2:
                return (val1, "greater than", val2)
            elif val1 < val2:
                return (val1, "less than", val2)
            else:
                return (val1, "equal to", val2)
        elif isinstance(val1, str) and isinstance(val2, str):
            if val1 > val2:
                return (val1, "greater than", val2)
            elif val1 < val2:
                return (val1, "less than", val2)
            else:
                return (val1, "equal to", val2)
        else:
            raise TypeError("Both values must be either numeric or strings")

if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare_values(10, 5)
    result2 = comparator.compare_values('apple', 'banana')
    print(result1)
    print(result2)