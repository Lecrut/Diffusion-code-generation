class NumericComparator:
    def is_strictly_greater(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numeric types.")
        try:
            return a > b
        except OverflowError:
            raise ValueError("Numeric overflow detected during comparison.")
if __name__ == '__main__':
    comparator = NumericComparator()
    result_1 = comparator.is_strictly_greater(5, 3)
    print(f"Integers (5 > 3): {result_1}")
    result_2 = comparator.is_strictly_greater(4.789, 4.0)
    print(f"Floats (4.789 > 4.0): {result_2}")
    result_3 = comparator.is_strictly_greater(5, 4.1)
    print(f"Mixed (5 > 4.1): {result_3}")
    try:
        comparator.is_strictly_greater("ten", "five")
    except TypeError as e:
        print(f"Caught expected error for non-numbers: {e}")