def check_equivalence(expr1, expr2):
    if isinstance(expr1, bool) and isinstance(expr2, bool):
        return expr1 == expr2
    if isinstance(expr1, list) and isinstance(expr2, list):
        if len(expr1) != len(expr2):
            return False
        for b1, b2 in zip(expr1, expr2):
            if b1 != b2:
                return False
        return True
    return False
if __name__ == '__main__':
    print(check_equivalence(True, True))
    print(check_equivalence(True, False))
    print(check_equivalence([True, False], [True, False]))
    print(check_equivalence([True, False], [False, True]))
    print(check_equivalence([True, True, False], [True, True, False]))
    print(check_equivalence([True, False], [True, False, True]))
    print(check_equivalence(False, False))
    print(check_equivalence(True, False))