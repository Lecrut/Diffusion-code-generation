class ValueComparator:

    def compare(self, val1, val2):
        if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
            raise ValueError('Both values must be integers or floats')
        if val1 > val2:
            return f'{val1} is greater than {val2}'
        elif val1 < val2:
            return f'{val1} is less than {val2}'
        else:
            return f'{val1} is equal to {val2}'
if __name__ == '__main__':
    comparator = ValueComparator()
    try:
        result = comparator.compare(10, 5)
        print(result)
        result = comparator.compare(3.5, 7.2)
        print(result)
        result = comparator.compare(4, 4)
        print(result)
        result = comparator.compare('a', 4)
    except ValueError as e:
        print(e)