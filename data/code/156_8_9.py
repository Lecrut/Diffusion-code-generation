def compute_mean(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    result = compute_mean(sample_data)
    print(result)