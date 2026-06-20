def validate_inputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numeric values")

def swap_values(a, b):
    validate_inputs(a, b)
    values = [a, b]
    values[0], values[1] = values[1], values[0]
    return values

if __name__ == '__main__':
    x, y = 5, 10
    swapped = swap_values(x, y)
    print(f"Swapped values: x={swapped[0]}, y={swapped[1]}")