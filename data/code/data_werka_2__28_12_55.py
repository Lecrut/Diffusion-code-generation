class ValueComparator:
    def __init__(self, value1: float, value2: float):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def is_float(value) -> bool:
        return isinstance(value, float)

    def compare(self) -> bool:
        if not self.is_float(self.value1):
            raise ValueError("The first input must be a float.")
        if not self.is_float(self.value2):
            raise ValueError("The second input must be a float.")
        return self.value1 > self.value2

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 3.14
    SAMPLE_VALUE_2 = 2.71
    comparator = ValueComparator(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    result = comparator.compare()
    print(result)