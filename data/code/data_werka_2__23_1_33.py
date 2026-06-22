class ValueComparator:
    def compare(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            if val1 > val2:
                return f"{val1} is greater than {val2}"
            elif val1 < val2:
                return f"{val1} is less than {val2}"
            else:
                return f"{val1} is equal to {val2}"
        else:
            raise ValueError("Both values must be either integers or floats")

if __name__ == '__main__':
    comparator = ValueComparator()
    result = comparator.compare(15, 30)
    print(result)
    result = comparator.compare(25, 10)
    print(result)
    result = comparator.compare(7, 7)
    print(result)