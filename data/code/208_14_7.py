def calculate_mean(numbers):
    total = 0
    count = len(numbers)
    for number in numbers:
        total += number
    return total / count

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(calculate_mean(sample_values))