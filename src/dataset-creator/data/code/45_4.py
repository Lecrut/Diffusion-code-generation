def safe_sum(a: int | float, b: int | float) -> int | float:
    return sum(map(lambda x, y: (type(x).__name__ == type(y).__name__) and x + y if isinstance(x, (int, float)) else None, [a], [b]))
if __name__ == '__main__':
    result = safe_sum(10.5, 20)