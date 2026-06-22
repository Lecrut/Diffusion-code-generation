def find_median(samples):
    sorted_samples = sorted(samples)
    n = len(sorted_samples)
    if n == 0:
        return None
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_samples[mid_index]
    else:
        return (sorted_samples[mid_index - 1] + sorted_samples[mid_index]) / 2
if __name__ == '__main__':
    sample_data1 = [1, 3, 5, 7, 9]
    sample_data2 = [4, 1, 8, 2, 6]
    sample_data3 = [10, 20, 30, 40]
    sample_data4 = []
    print(find_median(sample_data1))
    print(find_median(sample_data2))
    print(find_median(sample_data3))
    print(find_median(sample_data4))