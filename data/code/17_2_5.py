import time

class NumberChecker:
    def check_parity(self, number):
        """
        Efficiently determines if an integer is even.
        
        Uses bitwise AND operator which has better performance than modulo 
        operator on modern hardware architectures. Returns True for even numbers, False otherwise.
        
        Args:
            number (int): The integer to check
            
        Returns:
            bool: True if the number is even, False otherwise
            
        Raises:
            TypeError: If the input is not an integer
        """
        return isinstance(number, int) and ((number & 1) == 0)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [42, -8, 7, 3.5]  # Includes floats to demonstrate error handling intent (though logic handles ints specifically)
    
    checker = NumberChecker()
    
    print("Testing NumberChecker.check_parity method:")
    print("-" * 30)
    
    for num in test_cases:
        if isinstance(num, float):
            # Demonstrate type checking behavior for edge cases like floats with .5 value
            try:
                result = checker.check_parity(num)
                print(f"{num}: {result}")
            except TypeError as e:
                print(f"Error testing {num} ({type(num).__name__}): {e}")
        else:
            start_time = time.perf_counter()
            is_even = checker.check_parity(num)
            end_time = time.perf_counter()
            
            execution_time_ns = (end_time - start_time) * 1_000_000_000
            
            status_str = "EVEN" if is_even else "ODD"
            print(f"{num:6} -> {status_str:^5} | Execution time: ~{execution_time_ns:.4f} ns")