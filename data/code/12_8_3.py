def find_median(sequence):
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    mid = n // 2
    if n % 2 == 1:
        return sorted_seq[mid]
    else:
        return (sorted_seq[mid - 1] + sorted_seq[mid]) / 2

if __name__ == '__main__':
    sample_data_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sample_data_2 = [7, 8, 9, 10]
    sample_data_3 = [42]
    sample_data_4 = [1, 2]
    print(find_median(sample_data_1))
    print(find_median(sample_data_2))
    print(find_median(sample_data_3))
    print(find_median(sample_data_4))