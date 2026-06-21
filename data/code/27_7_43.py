class NumericComparer:
    @staticmethod
    def check_inequality(value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise ValueError("Both values must be numeric (int or float).")
        return value1 != value2

if __name__ == '__main__':
    sample_values = [42, 3.14]
    result = NumericComparer.check_inequality(sample_values[0], sample_values[1])
    print(result)