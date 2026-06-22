def generate_geometric_sequence(start, ratio, terms):
    if not all(isinstance(i, (int, float)) for i in [start, ratio]) or not isinstance(terms, int) or terms <= 0:
        raise ValueError("Invalid input: start and ratio must be numbers, and terms must be a positive integer.")
    
    return [start * (ratio ** i) for i in range(terms)]

if __name__ == '__main__':
    start_number = 5
    multiplier = 3
    num_terms = 8
    result = generate_geometric_sequence(start_number, multiplier, num_terms)
    print(result)