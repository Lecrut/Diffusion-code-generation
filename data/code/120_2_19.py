class ValueComparer:
    def are_values_equal(self, a, b):
        return a == b

if __name__ == '__main__':
    comparer = ValueComparer()
    print(comparer.are_values_equal(10, 10))
    print(comparer.are_values_equal("hello", "hello"))
    print(comparer.are_values_equal(5.5, 5.5))
    print(comparer.are_values_equal(True, True))
    print(comparer.are_values_equal([1, 2], [1, 2]))
    print(comparer.are_values_equal(None, None))