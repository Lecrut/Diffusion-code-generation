def custom_and(a, b):
    return int(a == 1 and b == 1)

def custom_or(a, b):
    return int(a == 1 or b == 1)

def custom_not(a):
    return int(a == 0)

if __name__ == '__main__':
    a_val = 1
    b_val = 0
    c_val = 1

    and_result = custom_and(a_val, b_val)
    or_result = custom_or(a_val, b_val)
    not_c_result = custom_not(c_val)

    print(and_result)
    print(or_result)
    print(not_c_result)