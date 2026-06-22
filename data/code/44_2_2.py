def compute_arithmetic_mean(values):
    total = sum(values)
    count = len(values)
    return total / count

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7, 4.1, 5.9]
    mean = compute_arithmetic_mean(sample_values)
    print(mean)