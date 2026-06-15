def calculate_pair_averages(pairs):
    if not pairs:
        return {"first_average": None, "second_average": None}
    sum_first = 0
    sum_second = 0
    count = len(pairs)
    for first, second in pairs:
        sum_first += first
        sum_second += second
    avg_first = sum_first / count
    avg_second = sum_second / count
    return {"first_average": avg_first, "second_average": avg_second}
if __name__ == '__main__':
    sample_pairs = [(10, 20), (30, 40), (50, 60)]
    result = calculate_pair_averages(sample_pairs)
    print(result)