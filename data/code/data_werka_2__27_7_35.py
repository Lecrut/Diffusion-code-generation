class NumericComparator:
    VALID_TYPES = (int, float)

    @staticmethod
    def validate_value(value):
        if not isinstance(value, NumericComparator.VALID_TYPES):
            raise ValueError("Value must be an integer or a float.")

    def __init__(self, value1, value2):
        self.validate_value(value1)
        self.validate_value(value2)
        self.value1 = value1
        self.value2 = value2

    def are_inequal(self):
        return self.value1 != self.value2

if __name__ == '__main__':
    sample_values = [42, 3.14]
    comparator = NumericComparator(sample_values[0], sample_values[1])
    result = comparator.are_inequal()
    print(result)