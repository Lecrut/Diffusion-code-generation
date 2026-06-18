def aggregate_sum(a: float, b: float, c: float) -> float:
    return sum((a, b, c))
if __name__ == '__main__':
    result = aggregate_sum(10, 20, 30)
    print(result)