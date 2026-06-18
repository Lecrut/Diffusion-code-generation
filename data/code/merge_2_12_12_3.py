def is_odd_arithmetic(n: int) -> bool:
    return n % 2 == 1
def is_odd_bitwise(n: int) -> bool:
    return (n & 1) != 0
if __name__ == '__main__':
    test_cases = [-5, -4, 3, 0, 7]
    print("Arithmetic Method Results:")
    for num in test_cases:
        result = is_odd_arithmetic(num)
        status = "Odd" if result else "Even"
        print(f"{num}: {status}")
    print("\nBitwise Method Results:")
    for num in test_cases:
        result = is_odd_bitwise(num)
        status = "Odd" if result else "Even"
        print(f"{num}: {status}")