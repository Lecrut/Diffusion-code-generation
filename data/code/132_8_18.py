def combine_flags(flag1, flag2):
    return flag1 | flag2
if __name__ == '__main__':
    result = combine_flags(5, 3)
    print(result)