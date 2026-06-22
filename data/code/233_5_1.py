def fill_block(width: int, height: int) -> str:
    return '\n'.join(['X' * width for _ in range(height)])

if __name__ == '__main__':
    print(fill_block(5, 3))