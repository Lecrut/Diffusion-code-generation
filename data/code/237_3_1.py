import math
def generate_geometric_sequence(start, multiplier):
    sequence = []
    current_term = float(start)
    for _ in range(15):
        sequence.append(current_term)
        current_term *= multiplier
    return sequence
if __name__ == '__main__':
    start_number = 2.0
    multiplier = 1.5
    result = generate_geometric_sequence(start_number, multiplier)
    print(result)