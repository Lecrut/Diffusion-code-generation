def calculate_mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_values)
    print(result)