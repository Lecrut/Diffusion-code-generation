def generate_geometric_sequence(n):
    a = 2
    r = 3
    sequence = []
    for i in range(n):
        term = a * (r ** i)
        sequence.append(term)
    return sequence
if __name__ == '__main__':
    N = 10
    result = generate_geometric_sequence(N)
    for term in result:
        print(term)