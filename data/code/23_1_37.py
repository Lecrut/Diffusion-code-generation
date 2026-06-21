class ValueComparator:
    def compare(self, val1, val2):
        self._validate_inputs(val1, val2)
        if val1 > val2:
            return f"{val1} is greater than {val2}"
        elif val1 < val2:
            return f"{val1} is less than {val2}"
        else:
            return f"{val1} is equal to {val2}"

    def _validate_inputs(self, val1, val2):
        if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
            raise ValueError("Both values must be integers or floats")

if __name__ == '__main__':
    comparator = ValueComparator()
    result = comparator.compare(5.5, 3)
    print(result)
    result = comparator.compare(7, 10)
    print(result)
    result = comparator.compare(4, 4)
    print(result)