def add_variables(a: int | float, b: int | float, c: int | float) -> int | float:
    return sum((a, b, c))
if __name__ == '__main__':
    result = add_variables(10, 20.5, -3)
    print(result)