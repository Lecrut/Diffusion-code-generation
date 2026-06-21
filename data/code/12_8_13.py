import heapq
from statistics import median

def extract_median(sequence):
    n = len(sequence)
    if n == 0:
        raise ValueError("Sequence must not be empty")
    if n % 2 == 1:
        return sequence[n // 2]
    else:
        return (sequence[n // 2 - 1] + sequence[n // 2]) / 2

def get_optimal_median(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence must not be empty")
    return statistics.median(sequence)

if __name__ == '__main__':
    import statistics

    sample_list = [7, 1, 3, 4, 6, 5, 8]
    sample_odd = extract_median(sample_list)
    print(sample_odd)

    sample_even = [2, 1, 4, 3]
    sorted_even = sorted(sample_even)
    sample_even_median = extract_median(sorted_even)
    print(sample_even_median)

    sample_large = [10, 2, 8, 4, 6, 1, 9, 3, 7, 5]
    optimized_median = get_optimal_median(sample_large)
    print(optimized_median)