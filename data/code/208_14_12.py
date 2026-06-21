def calculate_mean(data):
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
    return total / count if count > 0 else float('nan')

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(calculate_mean(sample_data))