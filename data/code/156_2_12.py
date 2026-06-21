def compute_average(values):
    if not values:
        return 0
    total = sum(values)
    count = len(values)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    avg = compute_average(sample_values)
    print(avg)