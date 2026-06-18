def aggregate_sum(a: int | float, b: int | float, c: int | float) -> int | float:
    return sum((a, b, c))
if __name__ == '__main__':
    result = aggregate_sum(10, 20.5, -3)
    print(result)