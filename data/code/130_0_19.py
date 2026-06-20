def is_zero(number):
    return abs(number) < 1e-9

if __name__ == '__main__':
    zero_value = 0
    non_zero_value = 5
    negative_zero_value = -0
    small_non_zero_value = 3.14 * 1e-10
    
    print(f"is_zero({zero_value}): {is_zero(zero_value)}")
    print(f"is_zero({non_zero_value}): {is_zero(non_zero_value)}")
    print(f"is_zero({negative_zero_value}): {is_zero(negative_zero_value)}")
    print(f"is_zero({small_non_zero_value}): {is_zero(small_non_zero_value)}")