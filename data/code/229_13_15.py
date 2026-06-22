def print_asterisk_grid(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer.")
    
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        print()

if __name__ == '__main__':
    grid_size = 15
    print_asterisk_grid(grid_size)