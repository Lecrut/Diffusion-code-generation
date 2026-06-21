def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    expr1 = False
    expr2 = (3 < 5)
    result = compare_booleans(expr1, expr2)
    print(result)