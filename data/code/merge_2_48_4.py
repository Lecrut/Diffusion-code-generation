def divide(first: float, second: float) -> float | None:
    if second != 0.0:
        return first / second
    return None
if __name__ == '__main__':
    result = divide(10, 2)
    print(result)