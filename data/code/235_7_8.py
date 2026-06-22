def generate_checkerboard(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
    pattern = []
    for i in range(size):
        row = ['X' if (i + j) % 2 == 0 else '.' for j in range(size)]
        pattern.append(''.join(row))
    
    return '\n'.join(pattern)

if __name__ == '__main__':
    checkerboard = generate_checkerboard(4)
    print(checkerboard)