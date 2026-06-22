INITIAL_VALUE = 1
MULTIPLIER = 3
ITERATIONS = 8

def generate_geometric_sequence():
    sequence = [INITIAL_VALUE]
    for _ in range(1, ITERATIONS):
        sequence.append(sequence[-1] * MULTIPLIER)
    return sequence

if __name__ == '__main__':
    print(generate_geometric_sequence())