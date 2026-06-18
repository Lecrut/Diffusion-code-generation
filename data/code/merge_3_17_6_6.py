def is_even_recursive(n: int) -> bool:
    """
    Recursively determine if a non-negative integer is even.
    
    The logic subtracts 2 from n until it reaches either 0 (even) or 1 (odd).
    Base cases handle the smallest values directly to avoid infinite recursion on odd numbers 
    that might otherwise decrement down to negative territory in an unguarded loop,
    though mathematically for non-negative integers stopping at 0/1 is sufficient.
    
    Args:
        n (int): A non-negative integer.
        
    Returns:
        bool: True if the number is even, False otherwise.
    """
    # Base cases
    if n == 0 or n == 1:
        return n % 2 == 0
    
    # Recursive step: reduce by 2 and check parity of the result
    return is_even_recursive(n - 2)

def is_even_modulo(n: int) -> bool:
    """
    Directly determine if a non-negative integer is even using modulo operator.
    
    Args:
        n (int): A non-negative integer.
        
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Sample values to test both functions without user input or external dependencies
    samples = [0, 1, 2, 3, 4, 5, 100]
    
    print("Testing is_even_recursive vs is_even_modulo:")
    for num in samples:
        recursive_result = is_even_recursive(num)
        modulo_result = is_even_modulo(num)
        
        # Verify correctness first
        assert recursive_result == modulo_result, f"Mismatch at {num}"
        
        print(f"Number: {num:>4} | Recursive Result: {'Even' if recursive_result else 'Odd'} | Modulo Result: {'Even' if modulo_result else 'Odd'}")

    # Efficiency Analysis (printed as part of the runnable module's output)
    analysis = """
Efficiency Critique:

1. Direct Modulo Approach (is_even_modulo):
   - Time Complexity: O(1). The operation is a single arithmetic check executed in constant time by hardware or optimized CPU instructions.
   - Space Complexity: O(1). No stack frames are created; it uses only the local variable for storage.
   
2. Recursive Approach (is_even_recursive):
   - Time Complexity: O(n/2) which simplifies to O(n). For a number n, the function makes approximately n/2 recursive calls before hitting a base case. This is linear time relative to the input magnitude.
   - Space Complexity: O(n). Each recursive call adds a frame to the call stack until the base case is reached. In Python, this can lead to recursion depth limits for large integers (typically around 1000 frames default), causing a RecursionError for very large inputs unless sys.setrecursionlimit() is adjusted manually or an iterative solution is used instead.
   
Conclusion: The modulo approach is significantly more efficient in terms of both time and space, especially as the input size grows. It avoids stack overflow risks entirely while performing fewer operations."""

    print("\n" + analysis)