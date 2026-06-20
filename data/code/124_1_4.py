def basic_arithmetic(a, b):
    try:
        return {
            'addition': a + b,
            'subtraction': a - b,
            'multiplication': a * b,
            'floor_division': a // b
        }
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    result = basic_arithmetic(10, 4)
    if result is not None:
        print(result)