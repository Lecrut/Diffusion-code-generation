def int_to_binary(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    return f"{n:b}"

if __name__ == '__main__':
    print(int_to_binary(10))
    print(int_to_binary(255))
    print(int_to_binary(1))
    print(int_to_binary(1024))