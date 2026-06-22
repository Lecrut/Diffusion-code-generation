def decimal_to_binary(n: int) -> str:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    return f"{n:b}"

if __name__ == '__main__':
    sample_values = [1, 2, 5, 10, 255, 1024]
    for value in sample_values:
        print(decimal_to_binary(value))