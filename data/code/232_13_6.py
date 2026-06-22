def validate_input(limit):
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer")

def print_growing_sequence(start=2, multiplier=1.5, terms=6):
    validate_input(terms)
    term = start
    for _ in range(terms):
        print(round(term))
        term *= multiplier

if __name__ == '__main__':
    print_growing_sequence()