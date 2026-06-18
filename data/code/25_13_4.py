x = 0 if False else None

if x == 0:
    print("True")
else:
    print("False")

# Example usage of the expression directly (as requested in the prompt logic)
result_expression = bool(x == 0)

def is_zero(val):
    return val == 0

print(f"Expression result for x={x}: {is_zero(x)}")

if __name__ == '__main__':
    # Test cases with hard-coded values
    test_values = [0, -1, 42]
    
    for val in test_values:
        print(f"x is zero? {bool(val == 0) if isinstance(val, (int, float)) else 'N/A'}")

# The concise idiomatic expression requested evaluates to True if x is zero, False otherwise.