import sys

class ComparisonTool:
    """A utility class designed to compare two values safely."""

    def check_greater(self, value1, value2):
        """
        Determines if the first provided value is strictly greater than 
        the second value. Handles potential type errors gracefully by catching exceptions.

        Args:
            value1 (Any): The first value to be compared.
            value2 (Any): The second value to be compared.

        Returns:
            bool: True if value1 > value2, False otherwise. If a TypeError 
                  occurs during comparison, it returns False instead of raising an exception.
        """
        try:
            return value1 > value2
        except (TypeError, ValueError):
            # Gracefully handle cases where types are incompatible or values cannot be compared
            return False

if __name__ == '__main__':
    tool = ComparisonTool()

    # Sample test case 1: Integers (Expected: True)
    result_1 = tool.check_greater(5, 3)
    print(f"Test 1 - Is 5 greater than 3? {result_1}")

    # Sample test case 2: Floats vs Integers (Expected: False due to float precision issues or just > logic resulting in false if inputs were different)
    # Let's do a clear true/false pair with floats.
    result_2 = tool.check_greater(3.9, 4.0)
    print(f"Test 2 - Is 3.9 greater than 4.0? {result_2}")

    # Sample test case 3: String comparison (Expected: True because '1' > '2' is False but we want a true result for demo or just valid logic)
    # Let's use strings where the first is indeed lexicographically greater in some context, 
    # though usually numeric types are preferred. Let's stick to strict numbers for clarity unless mixed types fail gracefully.
    # Actually, string comparison 'b' > 'a' works fine.
    result_3 = tool.check_greater('z', 'a')
    print(f"Test 3 - Is 'z' greater than 'a'? {result_3}")

    # Sample test case 4: Incompatible types (Expected: False due to exception handling)
    try:
        result_4 = tool.check_greater("hello", None)
        print(f"Test 4 - Comparing string and None? Result handled gracefully as: {result_4}")
    except Exception as e:
        # This block should theoretically not be reached due to internal exception handling in check_greater
        print(f"Unexpected error occurred during comparison: {e}")

    # Sample test case 5: Identical values (Expected: False)
    result_5 = tool.check_greater(10, 10)
    print(f"Test 5 - Is 10 greater than 10? {result_5}")