def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = (5, 15, 25, 35, 45, 55, 65, 75)
    result = calculate_total(sample_values)
    print(result)