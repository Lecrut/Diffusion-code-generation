def validate_input(start, difference, terms):
    if not all(isinstance(i, (int, float)) for i in [start, difference, terms]):
        raise ValueError("All input values must be numbers.")
    if terms <= 0:
        raise ValueError("Number of terms must be a positive integer.")

def generate_arithmetic_sequence(start, difference, terms):
    validate_input(start, difference, terms)
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    start = 3
    difference = 4
    terms = 15
    sequence = generate_arithmetic_sequence(start, difference, terms)
    print(sequence)