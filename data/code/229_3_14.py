def print_square(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
    for i in range(size):
        for j in range(size):
            print("*", end="")
        print()

if __name__ == '__main__':
    try:
        print_square(8)
    except ValueError as e:
        print(e)