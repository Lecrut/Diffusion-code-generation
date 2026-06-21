def compute_mean(data):
    total = 0
    count = len(data)
    for number in data:
        total += number
    return total / count

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    mean_value = compute_mean(sample_data)
    print(mean_value)