class ValueComparator:
    def __init__(self, value1: float, value2: float):
        if not isinstance(value1, float) or not isinstance(value2, float):
            raise ValueError("Both inputs must be floats.")
        self.value1 = value1
        self.value2 = value2

    def is_first_larger(self) -> bool:
        return self.value1 > self.value2

if __name__ == '__main__':
    sample_value1 = 3.14
    sample_value2 = 2.71
    comparator = ValueComparator(sample_value1, sample_value2)
    print(comparator.is_first_larger())