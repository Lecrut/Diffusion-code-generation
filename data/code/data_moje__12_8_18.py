import statistics
import math

def median_element(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_seq[mid - 1] + sorted_seq[mid]) / 2
    return sorted_seq[mid]

if __name__ == '__main__':
    odd_sample = [9, 3, 7, 1, 5]
    even_sample = [4, 2, 6, 8]
    single_sample = [10]
    mixed_sample = [-1, -5, 0, 5, 1, 10, -10]
    print(median_element(odd_sample))
    print(median_element(even_sample))
    print(median_element(single_sample))
    print(median_element(mixed_sample))