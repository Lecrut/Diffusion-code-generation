def validate_index(index):
    if not isinstance(index, int) or index < 0:
        raise ValueError("Index must be a non-negative integer")

def print_growing_number_sequence(limit=10):
    validate_index(limit)
    for i in range(limit):
        print(i**2)

if __name__ == '__main__':
    print_growing_number_sequence()