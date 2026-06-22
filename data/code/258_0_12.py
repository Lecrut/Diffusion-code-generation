def calculate_averages(data):
    sums = [0, 0]
    counts = [0, 0]
    for pair in data:
        if len(pair) >= 2:
            sums[0] += pair[0]
            counts[0] += 1
            sums[1] += pair[1]
            counts[1] += 1
    averages = [sums[i] / counts[i] if counts[i] > 0 else 0 for i in range(2)]
    return averages

if __name__ == '__main__':
    sample_data = [
        (10, 5),
        (20, 15),
        (30, 25)
    ]
    result = calculate_averages(sample_data)
    print(f"Average of first elements: {result[0]}")
    print(f"Average of second elements: {result[1]}")