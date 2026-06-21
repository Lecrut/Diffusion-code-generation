from decimal import Decimal, getcontext

def calculate_mean(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    
    total = Decimal(0)
    for value in values:
        total += Decimal(value)
    
    mean = total / Decimal(len(values))
    return mean

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3]
    getcontext().prec = 5
    result = calculate_mean(sample_values)
    print(result)