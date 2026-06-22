def compute_mean(values):
    total = sum(values)
    count = len(values)
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20]
    mean_value = compute_mean(sample_data)
    print(mean_value)