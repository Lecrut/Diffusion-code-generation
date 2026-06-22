def decimal_to_binary(n: int) -> str:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    return f"{n:b}"

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(1))