INITIAL_VALUE = 1
MULTIPLIER = 3
ITERATIONS = 8

def generate_geometric_sequence(start=INITIAL_VALUE, multiplier=MULTIPLIER, iterations=ITERATIONS):
    sequence = [start]
    for _ in range(iterations - 1):
        sequence.append(sequence[-1] * multiplier)
    return sequence

if __name__ == '__main__':
    print(generate_geometric_sequence())