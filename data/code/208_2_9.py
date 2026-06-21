def compute_mean(values):
    if not values:
        return None
    total = sum(values)
    count = len(values)
    average = total / count
    return average

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    mean_value = compute_mean(sample_data)
    print(mean_value)