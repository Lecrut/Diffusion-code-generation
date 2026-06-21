class ValueComparer:
    TOLERANCE = 1e-10

    @staticmethod
    def compare_values(a, b):
        return abs(a - b) > ValueComparer.TOLERANCE

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = ValueComparer.compare_values(value1, value2)
    print(result)