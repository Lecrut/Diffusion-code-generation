def validate_inputs(start, ratio, terms):
    if not isinstance(start, (int, float)) or start <= 0:
        raise ValueError("Start value must be a positive number.")
    if not isinstance(ratio, (int, float)) or ratio <= 0:
        raise ValueError("Ratio must be a positive number.")
    if not isinstance(terms, int) or terms <= 0:
        raise ValueError("Number of terms must be a positive integer.")

def generate_geometric_sequence(start, ratio, terms):
    validate_inputs(start, ratio, terms)
    return [start * (ratio ** i) for i in range(terms)]

if __name__ == '__main__':
    start_number = 5
    multiplier = 3
    term_count = 8
    result = generate_geometric_sequence(start_number, multiplier, term_count)
    print(result)