def is_even_recursive(n):
    """
    Recursively determine if a non-negative integer is even.
    
    Base case: 0 is even (True).
    Recursive step: n is even if n-1 is odd, and vice versa by decrementing until base case or negative numbers are reached.
    
    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if n is even, False otherwise.
    """
    # Base cases
    if n == 0:
        return True
    elif n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Recursive step
    # If current number is odd (n % 2 != 0), then subtracting 1 makes it even.
    # We can simply recurse on the next lower number and negate the result logic 
    # based on parity, but here we rely purely on decrementing until base case for strict recursion demonstration.
    # However, a simpler recursive definition: n is even iff (n-2) was processed as same parity? No.
    # Let's stick to simple decrement with alternating truth or check next odd/even.
    # Actually, standard reduction: Even(n) -> Odd(n+1). 
    # But without helper function for 'is_odd', we can just count steps if needed, but that's inefficient.
    
    # Efficient recursion logic within one function call structure using parity flip:
    # n is even <=> (n-2) has same parity? No, let's use the definition via subtraction of 1 and flipping result.
    return not is_even_recursive(n - 1)

def is_prime_modulo(n):
    """
    Direct modulo approach to check if a number is prime-like property for comparison context (not actually checking primality here).
    Wait, task asks specifically about 'even'. Let's use direct modulo as the efficient alternative.
    
    Args:
        n (int): A non-negative integer to check.
        
    Returns:
        bool: True if n is even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values as per requirements.
    samples = [0, 1, 2, 3, 4, 5, 6, 7]

    print("Testing Recursive Approach:")
    for num in samples:
        result_rec = is_even_recursive(num)
        status = "PASS" if (num % 2 == 0 and result_rec) or ((num % 2 != 0) and not result_rec) else "FAIL"
        print(f"is_even({num}) -> {result_rec} [{status}]")

    # Comparison of efficiency concepts:
    # Recursive approach involves stack depth proportional to n, making it O(n) time complexity due to repeated function calls.
    # It also uses O(n) space for the call stack in worst case.
    # Direct modulo approach is O(1) time and constant O(1) space as it performs a single arithmetic operation.

    print("\nTesting Modulo Approach:")
    for num in samples:
        result_mod = is_prime_modulo(num)  # Using the function defined above which implements n % 2 == 0 logic effectively
        status = "PASS" if (num % 2 == 0 and result_mod) or ((num % 2 != 0) and not result_mod) else "FAIL"
        print(f"is_even({num}) -> {result_mod} [{status}]")

    # Demonstrate that both yield identical results for the given samples.
    matches = all(is_even_recursive(x) == (x % 2 == 0) for x in range(10))
    if matches:
        print("\nBoth methods produced consistent results for integers up to 9.")