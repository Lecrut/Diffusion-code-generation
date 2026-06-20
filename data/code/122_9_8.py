from decimal import Decimal

NUMERIC_TYPES = (int, float)

def calculate_average(numbers):
    if not numbers:
        return Decimal('0')
    
    total = Decimal('0')
    count = 0
    
    for number in numbers:
        if isinstance(number, NUMERIC_TYPES):
            total += Decimal(str(number))
            count += 1
        else:
            raise ValueError("Invalid data type in input list")
    
    if count == 0:
        return Decimal('0')
    
    average = total / Decimal(count)
    return average

if __name__ == '__main__':
    sample_numbers = [3, 5.5, 2, 8.75]
    average = calculate_average(sample_numbers)
    print(average)