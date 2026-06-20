def are_flags_true(flag1, flag2):
    if not isinstance(flag1, int) or not isinstance(flag2, int):
        raise ValueError("Inputs must be integers")
    return (flag1 & 1 == 1) and (flag2 & 1 == 1)

if __name__ == '__main__':
    print(are_flags_true(3, 5))
    print(are_flags_true(4, 6))