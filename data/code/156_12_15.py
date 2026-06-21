def compute_average(values):
    if not values:
        return 0
    total_sum = sum(values)
    count = len(values)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_values = [12, 24, 36, 48, 60]
    avg = compute_average(sample_values)
    print(avg)