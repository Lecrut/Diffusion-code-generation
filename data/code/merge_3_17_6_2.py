def is_even_recursive(n: int) -> bool:
    """
    Recursively determine if a non-negative integer n is even.
    
    Logic: A number is even if it equals zero or if subtracting 2 repeatedly 
    leads to zero. This function checks the base case (n == 0) and reduces 
    the problem size by 2 in each recursive step.
    
    Args:
        n (int): Non-negative integer to check
        
    Returns:
        bool: True if even, False otherwise
    """
    # Base case: zero is even
    if n == 0:
        return True
    
    # Recursive case: decrement by 2; continue recursion until base case reached
    elif n < 0 or (n % 2 != 0): 
        # If already odd, it won't reach 0 by subtracting 2 exactly from even start,
        # but strictly following the "subtract 2" logic for evens:
        return is_even_recursive(n - 2)

    else:
        raise ValueError("Input must be non-negative")

def is_even_modulo(n: int) -> bool:
    """
    Direct modulo approach to determine if n is even.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        bool: True if even, False otherwise
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Sample test cases with hardcoded values
    sample_values = [0, 1, 2, 3, 4, 5, 100]

    print("Testing recursive is_even_recursive:")
    for val in sample_values:
        result_rec = is_even_recursive(val)
        status = "PASS" if (val % 2 == 0 and result_rec) or (val % 2 != 0 and not result_rec) else "FAIL"
        print(f"is_even_recursive({val}) -> {result_rec} | Expected: {val%2==0} [{status}]")

    print("\nTesting modulo is_even_modulo:")
    for val in sample_values:
        res = is_even_modulo(val)
        status = "PASS" if (val % 2 == 0 and res) or (val % 2 != 0 and not res) else "FAIL"
        print(f"is_even_modulo({val}) -> {res} | Expected: {val%2==0} [{status}]")

    # Efficiency Analysis Summary as comments since no prose output requested outside code logic blocks explicitly asked for docs elsewhere.
    """
    EFFICIENCY ANALYSIS CRITIQUE:
    
    1. Recursive Approach (is_even_recursive):
       - Time Complexity: O(n) in the worst case where n is even and large, because it decrements by 2 
         until reaching zero. For a number like 10^9, this requires ~5*10^8 recursive calls, causing stack overflow or extreme slowness.
       - Space Complexity: O(n) due to the call stack depth required for n steps.
       - Pros: Demonstrates recursion logic; no multiplication/division overhead per step if optimized by language (though Python has function call overhead).
       - Cons: Extremely inefficient for large integers compared to modulo operation.

    2. Modulo Approach (is_even_modulo):
       - Time Complexity: O(1) constant time regardless of input size, as modern CPUs compute modular arithmetic in hardware or via single instruction.
       - Space Complexity: O(1), no stack usage beyond local variables.
       - Pros: Instant execution; low memory footprint.
       - Cons: Requires understanding of bitwise logic (n & 1) which is equivalent to modulo by 2 but slightly more obscure for general audiences.

    Conclusion: The recursive approach should strictly avoid using integers larger than ~50-100 in practice due to Python's recursion limit and performance penalties.
    
    Bitwise Alternative Note: n % 2 == 0 can be replaced with (n & 1) == 0 for the same O(1) efficiency but is semantically identical here except for bitwise specialization context.
"""