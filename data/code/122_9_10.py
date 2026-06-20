from decimal import Decimal

def calculate_average(values):
    total = Decimal(0)
    count = 0
    for value in values:
        if isinstance(value, int):
            total += Decimal(str(value))
        elif isinstance(value, float):
            total += Decimal(str(value))
        count += 1
    return total / Decimal(count)

if __name__ == '__main__':
    sample_values = [1, 2.5, 3, 4.75]
    average = calculate_average(sample_values)
    print(average)