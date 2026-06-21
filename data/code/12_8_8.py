def extract_median(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    mid = n // 2
    if n % 2 == 1:
        return sorted_seq[mid]
    else:
        return (sorted_seq[mid - 1] + sorted_seq[mid]) / 2

if __name__ == '__main__':
    sample_data_1 = [7, 1, 3, 4, 2, 8, 5, 6, 9]
    sample_data_2 = [10, 20, 30, 40]
    sample_data_3 = [5]
    sample_data_4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    print(extract_median(sample_data_1))
    print(extract_median(sample_data_2))
    print(extract_median(sample_data_3))
    print(extract_median(sample_data_4))