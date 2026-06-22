def compute_average(values):
    total = sum(values)
    count = len(values)
    average = total / count if count > 0 else 0
    return average

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20]
    result = compute_average(sample_data)
    print(result)