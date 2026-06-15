import sys
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
    avg_first = sum_first / count_first if count_first > 0 else 0
    avg_second = sum_second / count_second if count_second > 0 else 0
    return avg_first, avg_second
if __name__ == '__main__':
    sample_pairs = [
        (10, 20),
        (5, 15),
        (3.5, 7.5),
        (2, 'invalid'),
        (8, 4)
    ]
    avg1, avg2 = calculate_averages(sample_pairs)
    print(f"Average of the first elements: {avg1}")
    print(f"Average of the second elements: {avg2}")