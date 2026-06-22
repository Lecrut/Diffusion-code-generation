def generate_geometric_sequence(start, ratio, terms):
    if not isinstance(start, (int, float)) or not isinstance(ratio, (int, float)) or not isinstance(terms, int):
        raise ValueError("Invalid input: start, ratio must be numbers and terms must be an integer.")
    
    if terms <= 0:
        raise ValueError("Invalid input: terms must be greater than zero.")
    
    return [start * (ratio ** i) for i in range(terms)]

if __name__ == '__main__':
    try:
        start_number = 5
        multiplier = 3
        term_count = 8
        result = generate_geometric_sequence(start_number, multiplier, term_count)
        print(result)
    except ValueError as e:
        print(e)