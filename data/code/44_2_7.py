def calculate_mean(values):
    if not values:
        return 0.0
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7, 4.1, 5.9]
    result = calculate_mean(sample_values)
    print(result)