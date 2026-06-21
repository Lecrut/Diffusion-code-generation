def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(calculate_total(sample_data))