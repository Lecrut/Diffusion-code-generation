def calculate_mean(data):
    total = 0
    count = len(data)
    for value in data:
        total += value
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_data))