def find_median(sequence):
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    mid = n // 2
    if n % 2 == 1:
        return sorted_seq[mid]
    else:
        return (sorted_seq[mid - 1] + sorted_seq[mid]) / 2.0

if __name__ == '__main__':
    sample_odd = [3, 1, 4, 1, 5, 9, 2]
    sample_even = [3, 1, 4, 1, 5, 9]
    sample_single = [42]
    sample_two = [10, 20]

    print(find_median(sample_odd))
    print(find_median(sample_even))
    print(find_median(sample_single))
    print(find_median(sample_two))