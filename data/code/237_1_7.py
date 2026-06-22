def validate_inputs(start, difference, terms):
    if not all(isinstance(x, (int, float)) for x in [start, difference, terms]):
        raise ValueError("All inputs must be numbers.")
    if terms < 1:
        raise ValueError("Number of terms must be a positive integer.")

def generate_arithmetic_sequence(start, difference, terms):
    validate_inputs(start, difference, terms)
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    start = 3
    difference = 4
    terms = 15
    sequence = generate_arithmetic_sequence(start, difference, terms)
    print(sequence)