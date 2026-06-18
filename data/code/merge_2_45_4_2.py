def safe_sum(a: int | float = 0, b: int | float = 0) -> None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    result = map(lambda x, y: x + y, [a], [b])
if __name__ == '__main__':
    try:
        safe_sum(10, 20)
    except Exception as e:
        print(f"Error: {e}")