def validate_input(n):
    if n < 1 or not isinstance(n, int):
        raise ValueError("Input must be a positive integer")

def print_growing_sequence(start=2, multiplier=1.5, terms=6):
    validate_input(terms)
    current_term = start
    for _ in range(terms):
        print(round(current_term))
        current_term *= multiplier

if __name__ == '__main__':
    print_growing_sequence()