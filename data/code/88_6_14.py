def are_flags_true(flag1, flag2):
    return (flag1 & 1) != 0 and (flag2 & 1) != 0

if __name__ == '__main__':
    print(are_flags_true(3, 5))