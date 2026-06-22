class NumericInequality:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def are_inequal(self):
        if not isinstance(self.value1, (int, float)) or not isinstance(self.value2, (int, float)):
            raise ValueError("Both values must be numeric (int or float).")
        return self.value1 != self.value2

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 42
    SAMPLE_VALUE_2 = 3.14
    inequality_checker = NumericInequality(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    result = inequality_checker.are_inequal()
    print(result)