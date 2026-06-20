class ValueComparator:
    @staticmethod
    def are_values_equal(a, b):
        return a == b

if __name__ == '__main__':
    comparator = ValueComparator()
    print(comparator.are_values_equal(5, 5))
    print(comparator.are_values_equal(3, 7))