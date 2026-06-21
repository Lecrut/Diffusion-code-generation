from decimal import Decimal, getcontext

def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    total = Decimal(0)
    for number in numbers:
        total += Decimal(str(number))
    
    return total / Decimal(len(numbers))

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3]
    try:
        mean_value = calculate_mean(sample_values)
        print(f"The mean is: {mean_value}")
    except ValueError as e:
        print(e)