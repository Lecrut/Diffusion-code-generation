class ValueComparer:
    @staticmethod
    def are_values_equal(a, b):
        return a == b

if __name__ == '__main__':
    print(ValueComparer.are_values_equal(5, 5))
    print(ValueComparer.are_values_equal(3, 7))