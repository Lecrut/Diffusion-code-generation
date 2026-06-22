import statistics

def find_median(sequence):
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    if n % 2 == 1:
        return sorted_seq[n // 2]
    else:
        return (sorted_seq[n // 2 - 1] + sorted_seq[n // 2]) / 2

if __name__ == '__main__':
    sample_data_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sample_data_2 = [10, 20, 30, 40]
    sample_data_3 = [7]
    
    print(find_median(sample_data_1))
    print(find_median(sample_data_2))
    print(find_median(sample_data_3))