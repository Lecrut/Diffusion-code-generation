class ValueComparer:
    @staticmethod
    def are_values_equal(a, b):
        return a == b

if __name__ == '__main__':
    result1 = ValueComparer.are_values_equal(1, 1)
    result2 = ValueComparer.are_values_equal(5, 5)
    result3 = ValueComparer.are_values_equal(1, 2)
    result4 = ValueComparer.are_values_equal(10, 10)
    print(f"result1: {result1}")
    print(f"result2: {result2}")
    print(f"result3: {result3}")
    print(f"result4: {result4}")