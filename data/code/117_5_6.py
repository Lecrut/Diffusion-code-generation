def calculate_difference(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b

if __name__ == '__main__':
    result = calculate_difference(100.5, 45.2)
    print(result)