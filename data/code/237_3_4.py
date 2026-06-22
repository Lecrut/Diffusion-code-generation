def generate_geometric_sequence(start_value, ratio, terms):
    return [start_value * (ratio ** i) for i in range(terms)]

if __name__ == '__main__':
    print(generate_geometric_sequence(5, 3, 8))