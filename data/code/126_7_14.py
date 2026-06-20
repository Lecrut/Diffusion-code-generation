class ValueComparer:
    def are_values_equal(self, value1, value2):
        return value1 == value2

if __name__ == '__main__':
    comparer = ValueComparer()
    print(f"1 and 1: {comparer.are_values_equal(1, 1)}")
    print(f"5 and 5: {comparer.are_values_equal(5, 5)}")
    print(f"1 and 2: {comparer.are_values_equal(1, 2)}")
    print(f"10 and 10.0: {comparer.are_values_equal(10, 10.0)}")