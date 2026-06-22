from decimal import Decimal, InvalidOperation

def calculate_triangle_area(base_value, height_value):
    try:
        base = Decimal(str(base_value))
        height = Decimal(str(height_value))
    except (InvalidOperation, ValueError):
        raise ValueError("Input values must be valid numbers")
    
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive values")
    
    return (base * height) / Decimal('2')

if __name__ == '__main__':
    sample_base = 15.75
    sample_height = 8.3
    result = calculate_triangle_area(sample_base, sample_height)
    print(result)