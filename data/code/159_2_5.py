def validate_range(start, end):
    if start < 1 or end > 100:
        raise ValueError("Range must be between 1 and 100 inclusive.")
    if start >= end:
        raise ValueError("Start of range must be less than the end.")

def generate_odd_numbers():
    validate_range(1, 100)
    return list(range(1, 101, 2))

if __name__ == '__main__':
    odd_numbers = generate_odd_numbers()
    print(odd_numbers)