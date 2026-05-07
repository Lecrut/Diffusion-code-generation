def check_both_true(flag1, flag2):
    return (flag1 & flag2) == flag1
if __name__ == '__main__':
    a = 1
    b = 1
    print(check_both_true(a, b))
    a = 1
    b = 0
    print(check_both_true(a, b))
    a = 0
    b = 1
    print(check_both_true(a, b))
    a = 0
    b = 0
    print(check_both_true(a, b))
    a = 3                
    b = 3                
    print(check_both_true(a, b))