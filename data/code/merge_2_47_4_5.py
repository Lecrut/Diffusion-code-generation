import sys
def multiply_large_integers(a: int, b: int) -> int:
    return a * b
if __name__ == '__main__':
    val_a = 123456789012345678901234567890
    val_b = 987654321098765432109876543210
    result = multiply_large_integers(val_a, val_b)
    print(f"Input A: {val_a}")
    print(f"Input B: {val_b}")
    print(f"Result:   {result}")