import math

def compute_mean(sequence: list) -> float:
    if not sequence:
        return 0.0
    total = math.fsum(sequence)
    count = len(sequence)
    return total / count

if __name__ == '__main__':
    sample_sequence = [12, 24, 36, 48, 60]
    print(compute_mean(sample_sequence))