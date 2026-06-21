def compute_mean(data):
    if not data:
        return 0
    total_sum = sum(data)
    count = len(data)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(f"Average: {result}")