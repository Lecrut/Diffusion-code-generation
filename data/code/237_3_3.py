def generate_geometric_sequence(start, ratio, terms):
    return [start * (ratio ** i) for i in range(terms)]

if __name__ == '__main__':
    start_number = 5
    multiplier = 3
    result = generate_geometric_sequence(start_number, multiplier, 8)
    print(result)