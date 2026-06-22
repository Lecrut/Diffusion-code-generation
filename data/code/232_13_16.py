def validate_inputs(limit):
    if not isinstance(limit, int) or limit < 1:
        raise ValueError("Limit must be a positive integer")

def generate_growing_sequence():
    term = 2
    for _ in range(6):
        print(round(term))
        term *= 1.5

if __name__ == '__main__':
    validate_inputs(6)
    generate_growing_sequence()