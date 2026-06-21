def compute_mean(data):
    total = sum(data)
    count = len(data)
    average = total / count if count > 0 else 0
    return average

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    result = compute_mean(sample_values)
    print(result)