def _build_row(size: int) -> str:
    if size <= 0:
        raise ValueError("Size must be a positive integer")
    return '*' * size

def create_square(size: int) -> str:
    if size <= 0:
        raise ValueError("Size must be a positive integer")
    row = _build_row(size)
    return (row + '\n') * size

if __name__ == '__main__':
    side_length = 7
    try:
        output = create_square(side_length)
        print(output, end='')
    except ValueError as e:
        print(f"Error: {e}")