def compute_means(data):
    if not data:
        return 0, 0
    sum_first = 0
    sum_second = 0
    count = len(data)
    for first, second in data:
        sum_first += first
        sum_second += second
    mean_first = sum_first / count
    mean_second = sum_second / count
    return mean_first, mean_second
if __name__ == '__main__':
    sample_data_1 = [(10, 20), (30, 40), (50, 60)]
    sample_data_2 = [(1, 2), (3, 4), (5, 6)]
    empty_data = []
    mean1_1, mean2_1 = compute_means(sample_data_1)
    print(f"Mean of first numbers for sample 1: {mean1_1}")
    print(f"Mean of second numbers for sample 1: {mean2_1}")
    mean1_2, mean2_2 = compute_means(sample_data_2)
    print(f"Mean of first numbers for sample 2: {mean1_2}")
    print(f"Mean of second numbers for sample 2: {mean2_2}")
    mean1_empty, mean2_empty = compute_means(empty_data)
    print(f"Mean of first numbers for empty data: {mean1_empty}")
    print(f"Mean of second numbers for empty data: {mean2_empty}")