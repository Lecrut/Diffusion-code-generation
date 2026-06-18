import timeit

def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise AND operation with 1.
    
    An integer n is odd if and only if its least significant bit (LSB) is set to 1.
    The expression (n & 1) evaluates the LSB directly without division or modulo operations.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is odd, False otherwise.
    """
    return (n & 1) == 1

def main():
    # Hard-coded sample values for testing without user input or arguments
    samples = [0, 1, -32, -5, 4294967295]

    print("Testing is_odd_bitwise function:")
    
    # Verify correctness on known odd and even numbers including negatives
    test_cases_correctness = {
        0: False,      # Even
        1: True,       # Odd
        -32: False,    # Negative even (binary ends in ...0)
        -5: True,      # Negative odd (two's complement ends in ...1)
        4294967295: True  # Large positive odd
    }

    all_passed = True
    for num, expected_is_odd in test_cases_correctness.items():
        result = is_odd_bitwise(num)
        status = "PASS" if result == expected_is_odd else "FAIL"
        print(f"{num}: Expected {expected_is_odd}, Got {result} -> {status}")
        all_passed and (all_passed := False)

    # Performance comparison: Bitwise vs Modulo on a tight loop
    iterations = 10_000_000
    
    time_bitwise = timeit.timeit(
        stmt=f"is_odd_bitwise({2**31 + 1})", 
        number=iterations, 
        setup="from __main__ import is_odd_bitwise"
    )

    def is_odd_modulo(n: int) -> bool:
        return n % 2 != 0
    
    time_modulo = timeit.timeit(
        stmt=f"is_odd_modulo({2**31 + 1})", 
        number=iterations, 
        setup="from __main__ import is_odd_modulo"
    )

    print(f"\nPerformance Benchmark ({iterations:,} iterations):")
    print(f"Bitwise method time: {time_bitwise:.4f}s")
    print(f"Modulo method time:  {time_modulo:.4f}s")
    
    if time_bitwise < time_modulo:
        speedup = (time_modulo / time_bitwise) * 100
        print(f"\nBitwise approach is approximately {speedup:.2f}% faster.")
        
if __name__ == '__main__':
    main()