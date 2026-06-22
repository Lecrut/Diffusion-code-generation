def generate_geometric_sequence(start, multiplier, terms):
    if not isinstance(start, (int, float)) or not isinstance(multiplier, (int, float)) or not isinstance(terms, int):
        raise ValueError("Start value and multiplier must be numbers, and terms must be an integer.")
    if terms <= 0:
        raise ValueError("Number of terms must be positive.")
    
    sequence = []
    current_term = start
    for _ in range(terms):
        sequence.append(current_term)
        current_term *= multiplier
    return sequence

if __name__ == '__main__':
    start_number = 5
    multiplier = 3
    result = generate_geometric_sequence(start_number, multiplier, 8)
    print(result)