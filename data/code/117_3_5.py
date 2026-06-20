from decimal import Decimal

def calculate_monetary_difference(value1, value2):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise ValueError("Both inputs must be numeric")
    
    return Decimal(str(value1)) - Decimal(str(value2))

if __name__ == '__main__':
    try:
        sample_value1 = 10.50
        sample_value2 = 3.25
        result = calculate_monetary_difference(sample_value1, sample_value2)
        print(result)
    except ValueError as e:
        print(e)