def conditional_sum(a: int | float, b: int | float, c: int | float) -> int | None:
    if all(isinstance(x, (int, float)) for x in [a, b, c]):
        return a + b + c
    return None
if __name__ == '__main__':
    result = conditional_sum(10.5, 20, "30")
    print(result)