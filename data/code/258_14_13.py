def calculate_averages(pairs):
    sum_first = 0
    count_first = 0
    sum_second = 0
    count_second = 0
    for pair in pairs:
        if len(pair) == 2:
            try:
                num1 = float(pair[0])
                num2 = float(pair[1])
                sum_first += num1
                count_first += 1
                sum_second += num2
                count_second += 1
            except ValueError:
                print(f"Error: Invalid numeric value found in pair {pair}. Skipping.")
        else:
            print(f"Error: Pair {pair} does not contain exactly two elements. Skipping.")
    if count_first > 0:
        average_first = sum_first / count_first
    else:
        average_first = None
    if count_second > 0:
        average_second = sum_second / count_second
    else:
        average_second = None
    return average_first, average_second

if __name__ == '__main__':
    sample_pairs = [
        (10, 20),
        (30, 40),
        ('a', 50)
    ]
    avg_first, avg_second = calculate_averages(sample_pairs)
    print(f"Average of the first elements: {avg_first}")
    print(f"Average of the second elements: {avg_second}")