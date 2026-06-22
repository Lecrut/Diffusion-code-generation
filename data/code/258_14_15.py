def calculate_averages(pairs):
    sums = [0.0] * 2
    counts = [0] * 2
    for pair in pairs:
        if len(pair) == 2:
            try:
                num1, num2 = map(float, pair)
                sums[0] += num1
                counts[0] += 1
                sums[1] += num2
                counts[1] += 1
            except ValueError:
                continue
    averages = [sums[i] / counts[i] if counts[i] > 0 else None for i in range(2)]
    return averages

if __name__ == '__main__':
    sample_pairs = [
        (10, 20),
        (3.5, 4.5),
        ('a', 5),
        (6, 'b'),
        (7, 8)
    ]
    result = calculate_averages(sample_pairs)
    print(f"Averages: {result}")