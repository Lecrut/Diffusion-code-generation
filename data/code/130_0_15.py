def is_zero(number):
    return abs(number) < 1e-9

if __name__ == '__main__':
    zero = 0
    value1 = 5
    value2 = -0
    value3 = 3.14
    value4 = '0'
    
    print(f"is_zero({zero}): {is_zero(zero)}")
    print(f"is_zero({value1}): {is_zero(value1)}")
    print(f"is_zero({value2}): {is_zero(value2)}")
    print(f"is_zero({value3}): {is_zero(value3)}")
    print(f"is_zero({value4}): {is_zero(value4)}")