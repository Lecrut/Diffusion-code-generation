def combine_booleans(flag1, flag2):
    return flag1 and flag2
if __name__ == '__main__':
    a = True
    b = False
    result = combine_booleans(a, b)
    print(result)
    a = True
    b = True
    result = combine_booleans(a, b)
    print(result)
    a = False
    b = True
    result = combine_booleans(a, b)
    print(result)