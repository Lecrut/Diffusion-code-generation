def create_checkerboard(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
    return [[(i + j) % 2 for j in range(size)] for i in range(size)]

if __name__ == '__main__':
    size = 8
    checkerboard = create_checkerboard(size)
    print(checkerboard)