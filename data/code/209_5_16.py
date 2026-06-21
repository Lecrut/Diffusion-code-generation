from decimal import Decimal, getcontext

def calculate_mean(data):
    if not data:
        raise ValueError("Input list is empty")
    
    total = Decimal(0)
    for value in data:
        total += Decimal(value)
    
    return total / len(data)

if __name__ == '__main__':
    sample_data = [0.1, 0.2, 0.3]
    getcontext().prec = 5
    mean_value = calculate_mean(sample_data)
    print(f"Mean: {mean_value}")