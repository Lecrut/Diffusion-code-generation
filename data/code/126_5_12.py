class ValueComparator:
    @staticmethod
    def verify_value_equality(a, b):
        return a == b

if __name__ == '__main__':
    comparator = ValueComparator()
    print(comparator.verify_value_equality(5, 5))
    print(comparator.verify_value_equality(5, '5'))
    print(comparator.verify_value_equality([1, 2], [1, 2]))
    print(comparator.verify_value_equality([1, 2], [2, 1]))