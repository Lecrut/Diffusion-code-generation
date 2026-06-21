from decimal import Decimal, getcontext

def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    total = Decimal(0)
    for number in numbers:
        total += Decimal(number)
    
    mean = total / Decimal(len(numbers))
    return mean

if __name__ == '__main__':
    sample_numbers = [0.1, 0.2, 0.3]
    try:
        result = calculate_mean(sample_numbers)
        print(f"The mean is: {result}")
    except ValueError as e:
        print(e)