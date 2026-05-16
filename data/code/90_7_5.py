def check_conditions(a, b, c, d):
    result = (a | b) | (c & d)
    return result != 0
if __name__ == '__main__':
    a_val = 5
    b_val = 3
    c_val = 6
    d_val = 1
    if check_conditions(a_val, b_val, c_val, d_val):
        print("Condition met")
    else:
        print("Condition not met")