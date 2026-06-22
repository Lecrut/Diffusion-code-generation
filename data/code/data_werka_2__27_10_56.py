class ValueComparer:
    def __init__(self, tolerance=1e-10):
        self.tolerance = tolerance

    def compare(self, value1, value2):
        return abs(value1 - value2) > self.tolerance

if __name__ == '__main__':
    comparer = ValueComparer()
    value1 = 10
    value2 = 10.00000000000001
    result1 = comparer.compare(value1, value2)
    print(result1)

    value3 = 10
    value4 = 10.0
    result2 = comparer.compare(value3, value4)
    print(result2)