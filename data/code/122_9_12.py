from decimal import Decimal

def calculate_average(numbers):
    total = Decimal(0)
    count = 0
    for number in numbers:
        total += Decimal(str(number))
        count += 1
    if count == 0:
        raise ValueError("Cannot compute average of an empty list")
    return total / Decimal(count)

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, 8.75]
    print(calculate_average(sample_values))