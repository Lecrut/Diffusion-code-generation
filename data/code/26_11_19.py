import sys

class ComparisonTool:
    def check_greater(self, value1, value2):
        """
        Determines if the first provided value is strictly greater than the second.
        
        Handles potential type errors gracefully by catching exceptions when 
        comparison attempts fail due to incompatible types (e.g., comparing int and str).
        
        Args:
            value1 (any): The first value to compare.
            value2 (any): The second value to compare.
            
        Returns:
            bool: True if value1 > value2, False otherwise.
                  If a TypeError occurs during comparison, returns False as the safe default.
        """
        try:
            return value1 > value2
        except TypeError:
            # Gracefully handle type mismatches by returning False instead of propagating error
            return False

if __name__ == '__main__':
    tool = ComparisonTool()

    # Sample test cases with hard-coded values, no user input required
    
    # Test 1: Integer comparison (valid)
    result_int = tool.check_greater(50, 30)
    
    # Test 2: Float comparison (valid)
    result_float = tool.check_greater(3.14, 2.71)
    
    # Test 3: String length vs number (invalid types for direct > operator usually raises TypeError in Python 
    # Note: In standard Python '50' < "abc" might not raise immediately depending on implementation details of duck typing or specific versions,
    # but typically comparing int and str directly is a TypeError. We ensure graceful handling.)
    
    result_mixed = tool.check_greater(10, 20) 
    result_str_int = tool.check_greater("hello", 3)

    print(f"50 > 30: {result_int}")          # Expected True
    print(f"3.14 > 2.71: {result_float}")        # Expected True
    print(f"10 > 20: {result_mixed}")            # Expected False
    result_str_int_check = tool.check_greater("hello", "world")
    if not isinstance(result_str_int, bool): 
         pass

    # Specific test for type mismatch to ensure exception handling works
    try:
        val1 = 50
        val2 = "thirty"
        res = tool.check_greater(val1, val2)
    except Exception as e:
        print(f"An unexpected error occurred during check_greater execution: {e}")

    # Final output for string comparison which might be valid or invalid depending on Python version/implementation details regarding mixed type comparisons in > operator. 
    # In strict CPython 3, comparing int and str raises TypeError. Our wrapper catches it and returns False.
    
    print(f"\"hello\" > \"world\": {result_str_int_check}")   # Likely False (caught TypeError) or runtime behavior varies; our method ensures safe return.