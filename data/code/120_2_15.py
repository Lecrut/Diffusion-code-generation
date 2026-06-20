class ValueComparator:
    @staticmethod
    def are_values_equal(a, b):
        return a == b

if __name__ == '__main__':
    print(ValueComparator.are_values_equal(10, 10))
    print(ValueComparator.are_values_equal("hello", "hello"))
    print(ValueComparator.are_values_equal(5.5, 5.5))
    print(ValueComparator.are_values_equal(True, True))
    print(ValueComparator.are_values_equal(1, 2))
    print(ValueComparator.are_values_equal([1, 2], [1, 2]))
    print(ValueComparator.are_values_equal(None, None))