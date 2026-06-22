def validate_size(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("*", end="")
            if (j + 1) % size == 0:
                print()

if __name__ == '__main__':
    sample_size = 8
    validate_size(sample_size)
    print_square(sample_size)