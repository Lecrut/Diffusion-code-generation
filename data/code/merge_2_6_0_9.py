class NumericChecker:
    def is_strictly_greater(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise TypeError("Both values must be numeric integers or floats.")
        return value1 > value2
if __name__ == '__main__':
    checker = NumericChecker()
    result_int_1 = checker.is_strictly_greater(5, 3)
    result_float_1 = checker.is_strictly_greater(4.7, 4.69)
    result_mixed = checker.is_strictly_greater(50, 49.9)
    print(f"Test Integers (>): {result_int_1}")            
    print(f"Test Floats (>): {result_float_1}")           
    print(f"Test Mixed (>): {result_mixed}")              
    try:
        checker.is_strictly_greater("5", 3)
    except TypeError as e:
        print(f"Caught expected error for non-numeric input: {e}")
    try:
        checker.is_strictly_greater(5, "three")
    except TypeError as e:
        print(f"Caught expected error for second argument being string: {e}")