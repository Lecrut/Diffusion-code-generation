def validate_numeric_values(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both values must be numeric")

def swap_values(a, b):
    validate_numeric_values(a, b)
    values = [a, b]
    values[0], values[1] = values[1], values[0]
    return values

if __name__ == '__main__':
    num1 = 15
    num2 = 25
    swapped = swap_values(num1, num2)
    print(f"Swapped values: {swapped}")