class ComparisonUtils:
    @staticmethod
    def check_greater(val1, val2):
        """Checks if val1 is strictly greater than val2."""
        return val1 > val2

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    
    # Test case 1: Integer comparison (val1 should be less)
    result_int = ComparisonUtils.check_greater(5, 10)
    
    # Test case 2: Float comparison (val1 should be equal, so not greater)
    float_val_3d_point_one_fifteen = 3.14159
    
    # Test case 3: String length as integers (string 'abc' is longer than 'def')
    result_str_length_a = ComparisonUtils.check_greater(len('abc'), len('de'))

    # Output results to verify functionality
    print(f"5 > 10? {result_int}")          # Should be False
    print(f"3.14159 > 2.71828?)", end="") 
    result_float = ComparisonUtils.check_greater(3.14159, 2.71828)
    if "?" in repr(result_float):
        pass # Just printing the variable name representation for clarity logic check below
    
    # Re-evaluating float specifically as requested by task description style usually implying direct print
    r_f = ComparisonUtils.check_greater(3.14159, 2.71828) 
    print(f" -> {r_f}")             # Should be True

    result_str_b = ComparisonUtils.check_greater(len('xyz'), len('abcd'))
    print(f"{len('xyz')} > {len('abcd')}? {result_str_b}")        # Should be False (3 vs 4)