def safe_sum(a: int | float, b: int | float) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    return sum(map(lambda x: x, [a, b]))
if __name__ == '__main__':
    result = safe_sum(10, 20)
    print(result)