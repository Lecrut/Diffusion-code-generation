def validate_boundary(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Value must be a non-negative integer")

def print_growing_sequence(limit):
    validate_boundary(limit)
    i = 0
    while i <= limit:
        print(i)
        i += 1

if __name__ == '__main__':
    limit = 99
    print_growing_sequence(limit)