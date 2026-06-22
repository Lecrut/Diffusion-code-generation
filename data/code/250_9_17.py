import math

def calculate_mean(sequence: list) -> float:
    return math.fsum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(calculate_mean(sample_sequence))