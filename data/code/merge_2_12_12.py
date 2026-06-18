def is_odd_arithmetic(n: int) -> bool:
    return n % 2 != 0
def is_odd_bitwise(n: int) -> bool:
    return (n & 1) == 1
if __name__ == '__main__':
    test_values = [3, -5, 42, 0, 7]
    print("Arithmetic Method Results:")
    for val in test_values:
        result = is_odd_arithmetic(val)
        print(f"{val}: {result}")
    print("\nBitwise Method Results:")
    for val in test_values:
        result = is_odd_bitwise(val)
        print(f"{val}: {result}")