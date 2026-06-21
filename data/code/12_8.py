def find_median(sequence):
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    if n % 2 == 1:
        return sorted_seq[n // 2]
    else:
        mid1 = sorted_seq[n // 2 - 1]
        mid2 = sorted_seq[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_data_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sample_data_2 = [7, 2, 9, 4]
    sample_data_3 = [10]
    print(find_median(sample_data_1))
    print(find_median(sample_data_2))
    print(find_median(sample_data_3))