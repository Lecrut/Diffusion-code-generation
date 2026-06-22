def fill_block(width: int, height: int) -> str:
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    
    block = '\n'.join(['X' * width for _ in range(height)])
    return block

if __name__ == '__main__':
    sample_width = 5
    sample_height = 3
    print(fill_block(sample_width, sample_height))