def is_zero(number):
    epsilon = 1e-9
    return abs(number) < epsilon

if __name__ == '__main__':
    value = -2.718281828459045e-09
    print(f"is_zero({value}): {is_zero(value)}")