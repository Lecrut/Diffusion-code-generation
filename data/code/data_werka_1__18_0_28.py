def is_strictly_greater(num1, num2):
    try:
        return float(num1) > float(num2)
    except ValueError:
        raise TypeError("Both inputs must be numbers")

if __name__ == '__main__':
    sample_values = [
        (5, 3),
        ('7.2', '7.1'),
        ('abc', 5),
        (4.5, 4.5)
    ]
    
    for val1, val2 in sample_values:
        try:
            result = is_strictly_greater(val1, val2)
            print(f"{val1} > {val2}: {result}")
        except TypeError as e:
            print(f"Error comparing {val1} and {val2}: {e}")