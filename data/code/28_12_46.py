class ValueComparator:
    def __init__(self, value1: float, value2: float):
        if not isinstance(value1, float) or not isinstance(value2, float):
            raise ValueError("Both inputs must be floats.")
        self.value1 = value1
        self.value2 = value2

    def is_value1_greater(self) -> bool:
        return self.value1 > self.value2

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 3.14159
    SAMPLE_VALUE_2 = 2.71828
    comparator = ValueComparator(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    result = comparator.is_value1_greater()
    print(result)