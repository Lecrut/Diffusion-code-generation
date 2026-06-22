def validate_range(start, end):
    if start < 0 or end > 10:
        raise ValueError("Range must be between 0 and 10")

def print_numbers():
    validate_range(0, 10)
    for i in range(10):
        print(i)

if __name__ == '__main__':
    print_numbers()