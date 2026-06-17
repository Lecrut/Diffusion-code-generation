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
    sample_data = [(10, 20), (5, 15), (2, 30)]
    mean1, mean2 = compute_means(sample_data)
    print(f"Mean of first numbers: {mean1}")
    print(f"Mean of second numbers: {mean2}")
    empty_data = []
    mean1_empty, mean2_empty = compute_means(empty_data)
    print(f"Mean of first numbers for empty list: {mean1_empty}")
    print(f"Mean of second numbers for empty list: {mean2_empty}")