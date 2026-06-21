from decimal import Decimal, InvalidOperation

def calculate_mean(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    
    total = Decimal(0)
    for value in values:
        try:
            total += Decimal(value)
        except InvalidOperation:
            raise ValueError("All elements must be numbers")
    
    return total / len(values)

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3]
    print(calculate_mean(sample_values))