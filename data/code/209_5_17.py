from decimal import Decimal, InvalidOperation

def calculate_mean(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    total = Decimal(0)
    for value in data:
        try:
            total += Decimal(value)
        except InvalidOperation:
            raise ValueError("All elements must be numbers")
    
    return total / len(data)

if __name__ == '__main__':
    sample_data = [0.1, 0.2, 0.3]
    try:
        mean_value = calculate_mean(sample_data)
        print(f"Mean: {mean_value}")
    except ValueError as e:
        print(e)