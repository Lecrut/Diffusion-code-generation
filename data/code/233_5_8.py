def fill_block(width: int, height: int) -> str:
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    
    return '\n'.join(['X' * width for _ in range(height)])

if __name__ == '__main__':
    WIDTH = 5
    HEIGHT = 3
    print(fill_block(WIDTH, HEIGHT))