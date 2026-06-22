def compute_mean(numbers):
    if not numbers:
        return 0
    total_sum = sum(numbers)
    count = len(numbers)
    return total_sum / count

if __name__ == '__main__':
    sample_values = [15, 25, 35]
    average = compute_mean(sample_values)
    print(average)