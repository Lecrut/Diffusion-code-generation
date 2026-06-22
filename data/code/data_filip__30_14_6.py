def int_to_binary(n: int) -> str:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return "0"
    return f"{n:b}"

if __name__ == '__main__':
    test_values = [0, 1, 2, 10, 42, 255, 1024]
    for value in test_values:
        print(int_to_binary(value))