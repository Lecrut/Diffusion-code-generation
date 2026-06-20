def subtract_amounts(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise ValueError("Both inputs must be numbers.")
    return a - b

if __name__ == '__main__':
    try:
        result = subtract_amounts(15, 7)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")