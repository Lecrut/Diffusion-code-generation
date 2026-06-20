from decimal import Decimal

def calculate_average(numbers):
    total = Decimal(0)
    count = 0
    for number in numbers:
        total += Decimal(str(number))
        count += 1
    return total / Decimal(count)

if __name__ == '__main__':
    sample_numbers = [3, 5.5, 7, 2.5]
    average = calculate_average(sample_numbers)
    print(average)