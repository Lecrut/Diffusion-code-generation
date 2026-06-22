START_VALUE = 5
RATIO = 3
TERMS = 8

def generate_geometric_sequence(start, ratio, terms):
    return [start * ratio ** i for i in range(terms)]
if __name__ == '__main__':
    result = generate_geometric_sequence(START_VALUE, RATIO, TERMS)
    print(result)