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
    print(compute_means(sample_data))
    empty_data = []
    print(compute_means(empty_data))
    another_sample = [(10, 20), (30, 40)]
    print(compute_means(another_sample))