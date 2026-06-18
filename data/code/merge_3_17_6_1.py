import sys

def is_even_recursive(n):
    """
    Recursively determines if a non-negative integer is even.
    
    Base case: 0 is even.
    Recursive step: n-1 has opposite parity to n.
    """
    if n == 0:
        return True
    
    # For positive integers, we decrement until hitting 0.
    # The call stack depth will be equal to the value of n.
    return not is_even_recursive(n - 1)

def is_even_modulo(n):
    """Standard iterative approach using modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access.
    test_values = [0, 1, 50, -7, 1_000_000]

    print("Testing Evenness Determination")
    print("-" * 30)

    # Process only non-negative values as per the recursive function's constraint.
    valid_inputs = [x for x in test_values if x >= 0]

    for num in valid_inputs:
        result_recursive = is_even_recursive(num)
        result_modulo = is_even_modulo(num)

        status_match = "OK" if result_recursive == result_modulo else "MISMATCH"
        
        print(f"Number: {num}")
        print(f"Recursive Result:   {result_recursive} (Depth would be ~{num})")
        print(f"Modulo Result:      {result_modulo}")
        print(f"Status:             {status_match}\n")

    # Demonstrate stack depth warning conceptually for large numbers.
    if sys.getrecursionlimit() > 0 and valid_inputs[2] < sys.getrecursionlimit():
        limit_check = is_even_recursive(valid_inputs[2])
        print(f"Large number ({valid_inputs[2]}): {limit_check}")