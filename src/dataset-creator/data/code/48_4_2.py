def first_divided_by_second(first: float, second: float) -> float | None:
    if second != 0:
        return first / second
    return None
if __name__ == '__main__':
    result = first_divided_by_second(10.5, 2)
    print(result)