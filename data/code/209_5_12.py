from decimal import Decimal, getcontext

def mean_of_list(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    total = Decimal(0)
    for number in numbers:
        total += Decimal(str(number))
    
    return total / Decimal(len(numbers))

if __name__ == '__main__':
    sample_numbers = [0.1, 0.2, 0.3]
    try:
        result = mean_of_list(sample_numbers)
        print(result)
    except ValueError as e:
        print(e)