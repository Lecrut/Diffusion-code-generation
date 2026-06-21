def get_median(sequence):
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    mid = n // 2
    if n % 2 == 1:
        return sorted_seq[mid]
    else:
        return (sorted_seq[mid - 1] + sorted_seq[mid]) / 2.0

if __name__ == '__main__':
    sample_data_1 = [3, 1, 2, 4, 5]
    sample_data_2 = [3, 1, 2, 4]
    sample_data_3 = [10, 20, 30, 40, 50, 60]

    print(get_median(sample_data_1))
    print(get_median(sample_data_2))
    print(get_median(sample_data_3))