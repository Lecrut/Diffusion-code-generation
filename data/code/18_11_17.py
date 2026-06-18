import time
from decimal import Decimal, getcontext

# Set precision high enough to handle very large integers accurately if needed as strings
getcontext().prec = 100

class ComparisonTool:
    """A tool class optimized for comparing two values."""

    def check_greater(self, value1, value2):
        """
        Compares two provided values and returns the result.
        
        Optimized to handle large numbers efficiently by converting them 
        directly if they are numeric types or attempting fast string comparison logic 
        before falling back to Decimal for arbitrary precision safety when necessary.

        Args:
            value1 (int, float, str): The first value to compare.
            value2 (int, float, str): The second value to compare.

        Returns:
            int: 1 if value1 > value2, -1 if value1 < value2, 0 otherwise.
        """
        # Handle direct numeric comparison for standard types first (fastest path)
        try:
            n1 = float(value1)
            n2 = float(value2)
            
            if isinstance(n1, int):
                return 1 if n1 > value2 else (-1 if n1 < value2 else 0)
            elif isinstance(n2, int):
                 # If one is already an integer and the other was converted to float (e.g. from string), 
                 # we need precise comparison. However, standard float might lose precision for huge ints.
                 pass
            
            if n1 > n2: return 1
            elif n1 < n2: return -1
            else: return 0

        except ValueError:
            pass
        
        # If conversion to float fails (e.g., very large integers that exceed float precision), 
        # use Decimal for arbitrary precision comparison. This is the safe fallback.
        
        try:
            d1 = Decimal(str(value1))
            d2 = Decimal(str(value2))
            
            if d1 > d2: return 1
            elif d1 < d2: return -1
            else: return 0
            
        except Exception:
            # Fallback to simple string comparison logic for non-numeric strings 
            # (e.g., "apple" vs "banana") assuming lexicographical order is desired if types mismatch.
            s1 = str(value1)
            s2 = str(value2)
            
            return 1 if s1 > s2 else (-1 if s1 < s2 else 0)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    tool = ComparisonTool()

    # Sample 1: Standard integers
    result_ints = tool.check_greater(5, 3)
    print(f"Integers (5 vs 3): {result_ints}") 

    # Sample 2: Large Integers that might lose precision in float conversion
    large_a = "9007199254740993" 
    large_b = "8007199254740993" 
    
    result_large_ints = tool.check_greater(large_a, large_b)
    print(f"Large Integers ({large_a} vs {large_b}): {result_large_ints}")

    # Sample 3: Float values
    result_floats = tool.check_greater(10.5, 9.8)
    print(f"Floats (10.5 vs 9.8): {result_floats}")

    # Sample 4: String comparison fallback
    result_strings = tool.check_greater("zebra", "apple")
    print(f"Strings ('zebra' vs 'apple'): {result_strings}")

    # Performance check simulation with a loop of large number comparisons
    start_time = time.time()
    
    test_val1 = 9007199254740993
    test_val2 = 8007199254740993
    
    # Run a loop to simulate performance on repeated large number checks
    for _ in range(1000):
        tool.check_greater(test_val1, test_val2)
    
    end_time = time.time()
    duration = end_time - start_time

    print(f"Performance Test (1000 iterations of large int comparison took {duration:.6f} seconds)")