def safe_sum(a: int | float, b: int | float) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    result = map(lambda x, y: x + y, [a], [b])
    print(sum(result))
if __name__ == '__main__':
    safe_sum(10, 20)