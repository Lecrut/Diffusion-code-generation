class ValueComparator:
    @staticmethod
    def are_values_equal(x, y):
        return x == y

if __name__ == '__main__':
    comparator = ValueComparator()
    x1 = 5
    y1 = 5
    result1 = comparator.are_values_equal(x1, y1)
    print(f"Checking equality between {x1} and {y1}: {result1}")
    x2 = 10
    y2 = 20
    result2 = comparator.are_values_equal(x2, y2)
    print(f"Checking equality between {x2} and {y2}: {result2}")
    x3 = 3.14
    y3 = 3.14
    result3 = comparator.are_values_equal(x3, y3)
    print(f"Checking equality between {x3} and {y3}: {result3}")