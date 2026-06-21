def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = calculate_total(sample_data)
    print(result)