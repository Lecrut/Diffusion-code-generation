def km_to_m(km):
    if not isinstance(km, (int, float)):
        raise ValueError("Input must be a number")
    if km < 0:
        raise ValueError("Input must be a non-negative number")
    return km * 1000

if __name__ == '__main__':
    test_values = [0, 1, 2.5, 100]
    for value in test_values:
        result = km_to_m(value)
        print(f"{value} km is {result} m")
    
    try:
        km_to_m(-5)
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        km_to_m("invalid")
    except ValueError as e:
        print(f"Error: {e}")