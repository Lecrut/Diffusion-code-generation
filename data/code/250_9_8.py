import math

def calculate_mean(sequence: list) -> float:
    return math.fsum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(calculate_mean(sample_sequence))