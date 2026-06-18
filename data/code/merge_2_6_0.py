class NumericValue:
    def is_strictly_greater_than(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Both operands must be numeric types.")
        return self > other
if __name__ == '__main__':
    val1 = 5.7
    val2 = 3
    try:
        result = NumericValue().is_strictly_greater_than(val1, val2)
        print(f"{val1} is strictly greater than {val2}: {result}")
        invalid_val = "ten"
        test_obj = NumericValue()
        try:
            test_obj.is_strictly_greater_than(invalid_val, val2)
        except TypeError as e:
            print(f"Caught expected error for '{invalid_val}': {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {type(e).__name__}: {e}")