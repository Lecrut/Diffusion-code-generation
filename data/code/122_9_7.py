from decimal import Decimal

def calculate_average(numbers):
    total = Decimal(0)
    count = 0
    for number in numbers:
        total += Decimal(str(number))
        count += 1
    if count == 0:
        return Decimal('NaN')
    average = total / Decimal(count)
    return average

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, 8.75]
    result = calculate_average(sample_values)
    print(result)