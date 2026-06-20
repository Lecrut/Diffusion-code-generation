def check_conditions(p: bool, q: bool) -> bool:
    first_condition = p and (not q)
    second_condition = not p and q
    return first_condition or second_condition
if __name__ == '__main__':
    sample1 = (True, False)
    sample2 = (False, True)
    sample3 = (True, True)
    sample4 = (False, False)
    print(check_conditions(*sample1))
    print(check_conditions(*sample2))
    print(check_conditions(*sample3))
    print(check_conditions(*sample4))