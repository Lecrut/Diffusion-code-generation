def are_equivalent(expr1, expr2):
    if isinstance(expr1, str) and expr1 == "True" and isinstance(expr2, str) and expr2 == "True":
        return True
    if isinstance(expr1, str) and expr1 == "False" and isinstance(expr2, str) and expr2 == "False":
        return True
    if isinstance(expr1, str) and expr1 == "True" and isinstance(expr2, str) and expr2 == "False":
        return False
    if isinstance(expr1, str) and expr1 == "False" and isinstance(expr2, str) and expr2 == "True":
        return False
    if isinstance(expr1, str) and expr1 == "True" and isinstance(expr2, str) and expr2 == "True":
        return True
    if isinstance(expr1, str) and expr1 == "False" and isinstance(expr2, str) and expr2 == "False":
        return True
    return False
if __name__ == '__main__':
    print(are_equivalent(True, True))
    print(are_equivalent(False, False))
    print(are_equivalent(True, False))
    print(are_equivalent(False, True))
    print(are_equivalent(True, False))
    print(are_equivalent(False, True))
    print(are_equivalent(True, True))
    print(are_equivalent(False, False))