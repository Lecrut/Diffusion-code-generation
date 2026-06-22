def validate_boundary(value):
    if not (0 <= value <= 99):
        raise ValueError("Value must be between 0 and 99")

def print_growing_sequence():
    i = 0
    while i <= 99:
        validate_boundary(i)
        print(i)
        i += 1

if __name__ == '__main__':
    print_growing_sequence()