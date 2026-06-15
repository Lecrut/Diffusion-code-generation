def calculate_average(samples):
    total = 0
    count = 0
    for sample in samples:
        if isinstance(sample, (int, float)):
            total += sample
            count += 1
    if count > 0:
        return total / count
    else:
        return 0
if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    try:
        samples = [float(x) for x in sample_input.split()]
        average = calculate_average(samples)
        print(average)
    except ValueError:
        print("Error: One or more inputs were not valid numbers.")