def is_odd_arithmetic(n: int) -> bool:
    return n % 2 == 1
def is_odd_bitwise(n: int) -> bool:
    return (n & 1) != 0
if __name__ == '__main__':
    test_values = [-5, -4, 3, 2, 7]
    print("Arithmetic Method Results:")
    for val in test_values:
        result = is_odd_arithmetic(val)
        print(f"{val}: {result}")
    print("\nBitwise Trick Results:")
    for val in test_values:
        result = is_odd_bitwise(val)
        print(f"{val}: {result}")