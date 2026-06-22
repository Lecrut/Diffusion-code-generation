def calculate_averages(pairs):
    sums = [0.0] * 2
    counts = [0] * 2
    for pair in pairs:
        if len(pair) == 2:
            try:
                num1, num2 = float(pair[0]), float(pair[1])
                sums[0] += num1
                counts[0] += 1
                sums[1] += num2
                counts[1] += 1
            except ValueError:
                print(f"Error: Invalid numeric value found in pair {pair}. Skipping.")
        else:
            print(f"Error: Pair {pair} does not contain exactly two elements. Skipping.")
    averages = [sums[i] / counts[i] if counts[i] > 0 else None for i in range(2)]
    return averages

if __name__ == '__main__':
    sample_pairs = [
        (15, 25),
        (30, 40),
        ('a', 50),
        (60, 'b'),
        (70, 80)
    ]
    result = calculate_averages(sample_pairs)
    print(f"Average of the first elements: {result[0]}")
    print(f"Average of the second elements: {result[1]}")