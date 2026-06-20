def logical_operators():
    a = True
    b = False

    and_result = a and b
    or_result = a or b
    not_a = not a

    return and_result, or_result, not_a

if __name__ == '__main__':
    and_result, or_result, not_a = logical_operators()
    print(f"AND: {and_result}")
    print(f"OR: {or_result}")
    print(f"NOT A: {not_a}")