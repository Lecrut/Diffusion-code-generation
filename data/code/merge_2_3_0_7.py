def is_even_bitwise(n):
    return (n & 1) == 0
if __name__ == '__main__':
    test_values = [0, -5, 42, -3, 100]
    for val in test_values:
        result = "Even" if is_even_bitwise(val) else "Odd"
        print(f"{val}: {result}")