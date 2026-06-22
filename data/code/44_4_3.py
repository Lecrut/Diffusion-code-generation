def calculate_mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = calculate_mean(sample_values)
    print(result)