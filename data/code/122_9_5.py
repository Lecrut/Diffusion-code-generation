from decimal import Decimal

def calculate_average(numbers):
    total = Decimal(0)
    count = 0
    for number in numbers:
        if isinstance(number, int):
            number = Decimal(number)
        total += number
        count += 1
    return total / count

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, 8.75]
    average = calculate_average(sample_values)
    print(average)