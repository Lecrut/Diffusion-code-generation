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
    sample_data = [(1, 2), (3, 4), (5, 6)]
    result = compute_means(sample_data)
    print(f"Mean of first numbers: {result[0]}")
    print(f"Mean of second numbers: {result[1]}")
    empty_data = []
    result_empty = compute_means(empty_data)
    print(f"Mean of first numbers for empty list: {result_empty[0]}")
    print(f"Mean of second numbers for empty list: {result_empty[1]}")
    sample_data_two = [(10, 20), (30, 40)]
    result_two = compute_means(sample_data_two)
    print(f"Mean of first numbers for second list: {result_two[0]}")
    print(f"Mean of second numbers for second list: {result_two[1]}")