def is_strictly_greater(num1, num2):
    try:
        return float(num1) > float(num2)
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    sample_values = [
        (5, 3),
        (3.5, 4.2),
        ('10', '5'),
        ('abc', 1),
        (7, 'seven')
    ]
    
    for val1, val2 in sample_values:
        result = is_strictly_greater(val1, val2)
        print(f"is_strictly_greater({val1}, {val2}) = {result}")