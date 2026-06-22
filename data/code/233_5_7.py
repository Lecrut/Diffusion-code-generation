def create_block(width: int, height: int) -> str:
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    
    block = []
    for _ in range(height):
        row = ['X'] * width
        block.append(''.join(row))
    
    return '\n'.join(block)

if __name__ == '__main__':
    WIDTH = 4
    HEIGHT = 6
    print(create_block(WIDTH, HEIGHT))