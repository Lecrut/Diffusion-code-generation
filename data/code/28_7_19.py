def sort_descending(a: float, b: float) -> list[float]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")
    if a > b:
        return [a, b]
    else:
        return [b, a]

if __name__ == '__main__':
    result = sort_descending(10, 5)
    print(result)