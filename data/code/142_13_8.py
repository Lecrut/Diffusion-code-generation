def compare_booleans(a: bool, b: bool) -> bool:
    return (a == b) or (a != b)

if __name__ == '__main__':
    expr1 = (3 < 5) and (7 != 9)
    expr2 = False
    if compare_booleans(expr1, expr2):
        print("Identical")
    else:
        print("Different")