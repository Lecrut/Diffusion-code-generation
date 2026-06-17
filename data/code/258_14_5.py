def calculate_averages(pairs):
    sum_first = 0
    count_first = 0
    sum_second = 0
    count_second = 0
    for a, b in pairs:
        if isinstance(a, (int, float)):
            sum_first += a
            count_first += 1
        if isinstance(b, (int, float)):
            sum_second += b
            count_second += 1
    avg_first = sum_first / count_first if count_first > 0 else 0
    avg_second = sum_second / count_second if count_second > 0 else 0
    return avg_first, avg_second
if __name__ == '__main__':
    sample_pairs = [
        (10, 20),
        (5, 15),
        (20, 30),
        (1, 1)
    ]
    try:
        avg1, avg2 = calculate_averages(sample_pairs)
        print(f"Average of the first elements: {avg1}")
        print(f"Average of the second elements: {avg2}")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")