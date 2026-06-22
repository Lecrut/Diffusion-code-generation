def calculate_mean(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = calculate_mean(sample_values)
    print(result)