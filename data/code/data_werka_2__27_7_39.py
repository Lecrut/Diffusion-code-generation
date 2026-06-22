class NumericComparator:
    @staticmethod
    def compare_inequality(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both values must be numeric (int or float).")
        return a != b

if __name__ == '__main__':
    value1 = 7
    value2 = 2.5
    result = NumericComparator.compare_inequality(value1, value2)
    print(result)