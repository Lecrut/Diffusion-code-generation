def validate_index(index):
    if not isinstance(index, int) or index < 0:
        raise ValueError("Index must be a non-negative integer")

def generate_sequence(limit):
    for i in range(limit):
        yield i**2

if __name__ == '__main__':
    limit = 10
    validate_index(limit)
    sequence = generate_sequence(limit)
    for num in sequence:
        print(num)