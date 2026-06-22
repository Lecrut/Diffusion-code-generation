def compute_mean(values):
    if not values:
        return 0
    total_sum = sum(values)
    count = len(values)
    return total_sum / count

if __name__ == '__main__':
    sample_values = [15, 25, 35]
    average = compute_mean(sample_values)
    print(average)