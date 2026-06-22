def compare_two_simple_quantities_now_transform(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be integers or floats")
    return a > b

if __name__ == '__main__':
    try:
        result = compare_two_simple_quantities_now_transform(5, 3)
        print(result)
    except ValueError as e:
        print(e)