class ValueComparer:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def compare(self):
        if isinstance(self.value1, (int, float)) and isinstance(self.value2, (int, float)):
            return max(self.value1, self.value2)
        else:
            raise ValueError("Both values must be integers or floats")

if __name__ == '__main__':
    sample_value1 = 45
    sample_value2 = 98.7
    comparer = ValueComparer(sample_value1, sample_value2)
    larger_value = comparer.compare()
    print(larger_value)