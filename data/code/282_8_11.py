INITIAL_VALUE = 0

def calculate_total(numbers):
    total = INITIAL_VALUE
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    sample_numbers = [10, -5, 3, -2, 4]
    result = calculate_total(sample_numbers)
    print(result)