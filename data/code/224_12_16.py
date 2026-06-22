def compute_average(values):
    total = sum(values)
    count = len(values)
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_data = [12, 18, 24, 30]
    average = compute_average(sample_data)
    print(average)