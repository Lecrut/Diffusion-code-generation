def calculate_mean(values):
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    sample_data = [1.5, 2.5, 3.0, 4.0, 5.5]
    result = calculate_mean(sample_data)
    print(result)