def is_zero(number):
    tolerance = 1e-9
    return abs(number) < tolerance

if __name__ == '__main__':
    value1 = 0
    value2 = 5
    value3 = -0
    value4 = 3.14
    value5 = '0'
    
    print(f"is_zero({value1}): {is_zero(value1)}")
    print(f"is_zero({value2}): {is_zero(value2)}")
    print(f"is_zero({value3}): {is_zero(value3)}")
    print(f"is_zero({value4}): {is_zero(value4)}")
    print(f"is_zero({value5}): {is_zero(value5)}")