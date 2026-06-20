from decimal import Decimal, getcontext

def calculate_average(numbers):
    if not numbers:
        return Decimal('0')
    
    total = Decimal('0')
    count = 0
    
    for number in numbers:
        total += Decimal(str(number))
        count += 1
    
    average = total / Decimal(count)
    return average

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, 8]
    result = calculate_average(sample_values)
    print(result)