def conditional_sum(a: int | float = 10, b: int | float = 20, c: int | float = 30) -> int | None:
    if all(isinstance(x, (int, float)) for x in [a, b, c]):
        return a + b + c
    else:
        return None
if __name__ == '__main__':
    result = conditional_sum(1.5, 2, "3")
    print(result)