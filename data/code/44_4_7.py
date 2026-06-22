def calculate_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_data)
    print(result)