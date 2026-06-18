def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise operations.
    
    The least significant bit (LSB) of any integer determines its parity:
    - If the LSB is 1, the number is odd.
    - If the LSB is 0, the number is even.
    
    This avoids the modulo operator and performs a single bitwise AND operation.
    
    Args:
        n (int): The integer to check
        
    Returns:
        bool: True if n is odd, False otherwise
    """
    return n & 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [0, 1, -2, -3, 42]
    
    print("Testing parity detection using bitwise AND:")
    for num in test_cases:
        result = is_odd_bitwise(num)
        expected = num % 2 != 0
        status = "PASS" if result == expected else "FAIL"
        odd_str = "Odd" if result else "Even"
        print(f"{num}: {odd_str} (Expected: {'Odd' if expected else 'Even'}, Status: {status})")

    # Demonstrate performance aspect by showing operation count for a few iterations
    import time
    
    num_samples = 10_000_000
    start_time = time.perf_counter()
    
    # Simulate checking parity many times using bitwise method
    _ = [is_odd_bitwise(i) for i in range(num_samples)]
    
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    
    print(f"\nPerformance Benchmark:")
    print(f"Checked {num_samples} integers ({elapsed:.4f} seconds)")
    print(f"Average operations per check: ~1 (single bitwise AND)")