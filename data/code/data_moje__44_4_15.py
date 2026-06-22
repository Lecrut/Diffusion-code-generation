def calculate_mean(numbers):
    total = 0
    count = 0
    for value in numbers:
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_values)
    print(result)