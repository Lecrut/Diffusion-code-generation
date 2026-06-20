def validate_numbers(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise ValueError("Both inputs must be numbers")

def swap_values(a, b):
    values = [a, b]
    values[0], values[1] = values[1], values[0]
    return values

if __name__ == '__main__':
    num1 = 42
    num2 = -7
    validate_numbers(num1, num2)
    swapped_values = swap_values(num1, num2)
    print(swapped_values)