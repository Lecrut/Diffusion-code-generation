from decimal import Decimal

def calculate_average(values):
    if not values:
        return Decimal('0')
    total = sum(Decimal(str(value)) for value in values)
    average = total / Decimal(len(values))
    return average

if __name__ == '__main__':
    sample_values = [1, 2.5, 3, 4.75]
    result = calculate_average(sample_values)
    print(result)