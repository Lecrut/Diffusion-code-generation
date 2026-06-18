def is_odd_arithmetic(n: int) -> bool:
    return n % 2 == 1
def is_odd_bitwise(n: int) -> bool:
    return (n & 1) == 1
if __name__ == '__main__':
    test_values = [-5, -4, 0, 3, 7, 8]
    print("Arithmetic Method Results:")
    for val in test_values:
        result = is_odd_arithmetic(val)
        status = "Odd" if result else "Even"
        print(f"{val}: {status}")
    print("\nBitwise Trick Results:")
    for val in test_values:
        result = is_odd_bitwise(val)
        status = "Odd" if result else "Even"
        print(f"{val}: {status}")