import timeit

def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise operations.
    
    An integer n is odd if its least significant bit (LSB) is 1.
    This can be checked by performing a bitwise AND with 1.
    If the result is non-zero, the number is odd; otherwise, it is even.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if n is odd, False otherwise.
    """
    return n & 1

def main():
    # Hard-coded sample values for testing without user input or command-line arguments
    test_cases = [0, 1, -5, 42, 63]

    print("Testing integer parity using bitwise AND operation:")
    
    for num in test_cases:
        result = is_odd_bitwise(num)
        status = "Odd" if result else "Even"
        print(f"{num} -> {status}")

if __name__ == '__main__':
    main()

# Performance comparison snippet (commented out as per instructions to not use sys.stdin/input())
# Uncommenting the following would allow a quick performance check in an interactive shell:
"""
import timeit

def is_odd_mod(n): return n % 2 != 0
def is_odd_bit(n): return n & 1

n = 10**6
mod_time = timeit.timeit('is_odd_mod(n)', setup=f'from __main__ import is_odd_mod; n={n}', number=10000)
bit_time = timeit.timeit('is_odd_bit(n)', setup=f'from __main__ import is_odd_bit; n={n}', number=10000)

print(f"Modulo method average: {mod_time:.6f}s")
print(f"Bitwise method average: {bit_time:.6f}s")
print(f"Savings factor (approx): {mod_time / bit_time}")
"""