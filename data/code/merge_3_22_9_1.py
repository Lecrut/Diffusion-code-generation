import timeit

def is_odd_bitwise(n: int) -> bool:
    """Check if an integer is odd using bitwise AND with 1."""
    return n & 1 != 0

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration
    samples = [3, -20, 0, 7]

    print("Testing 'is_odd_bitwise' function:")
    for num in samples:
        result = is_odd_bitwise(num)
        expected = num % 2 != 0
        status = "OK" if result == expected else "FAIL"
        print(f"is_odd({num}) -> {result} (expected {expected}) [{status}]")

    # Performance demonstration: compare bitwise vs modulo for large iterations
    setup_code = """\nimport timeit, random\nlarge_num = 2**63 - 1"""
    
    bit_ops_time = timeit.timeit(
        stmt="is_odd_bitwise(large_num)", 
        globals={}, 
        number=1_000_000
    )

    mod_op_time = timeit.timeit(
        stmt="(large_num % 2) != 0", 
        globals={"large_num": (lambda: large_num)}, 
        number=1_000_000
    )

    print(f"\nPerformance comparison over 1,000,000 iterations:")
    print(f"Bitwise operation time: {bit_ops_time:.4f} seconds")
    print(f"Modulo operation time:   {mod_op_time:.4f} seconds")