def to_binary_string(n: int) -> str:
    return f"{n:b}"

if __name__ == '__main__':
    sample_values = [0, 1, 10, 15, 100, 255, 1024, 65535]
    for value in sample_values:
        print(to_binary_string(value))