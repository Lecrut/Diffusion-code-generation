def validate_size(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")

def print_square(size):
    validate_size(size)
    for i in range(size):
        for j in range(size):
            print("*", end="")
        print()

if __name__ == '__main__':
    print_square(8)