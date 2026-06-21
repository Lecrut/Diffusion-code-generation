def check_equality(expr1: bool, expr2: bool) -> str:
    return "Identical" if expr1 == expr2 else "Different"

if __name__ == '__main__':
    sample1 = (2 * 3) == 6
    sample2 = False
    result = check_equality(sample1, sample2)
    print(result)