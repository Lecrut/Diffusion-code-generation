START = 1
FACTOR = 2
ITERATIONS = 5

def generate_growing_sequence(start=START, factor=FACTOR, iterations=ITERATIONS):
    sequence = []
    current_term = start
    for _ in range(iterations):
        sequence.append(current_term)
        current_term *= factor
    return sequence

if __name__ == '__main__':
    sequence = generate_growing_sequence()
    for term in sequence:
        print(term)