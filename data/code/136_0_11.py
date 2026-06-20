if __name__ == '__main__':
    a = True
    b = False

    print(f"a = {a}")
    print(f"b = {b}")

    and_result = a and b
    or_result = a or b
    not_a = not a

    print(f"Logical AND ({a} and {b}): {and_result}")
    print(f"Logical OR ({a} or {b}): {or_result}")
    print(f"Logical NOT ({a}): {not_a}")