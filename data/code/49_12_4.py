def print_square_grid(size: int = 8) -> list[str]:
    if size < 0:
        raise ValueError("Size must be non-negative")
    row = '*' * size
    return [row for _ in range(size)]

if __name__ == '__main__':
    sample_size = 8
    result = print_square_grid(sample_size)
    for line in result:
        print(line)