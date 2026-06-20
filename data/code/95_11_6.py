def check_conditions(a, b, c):
    is_a_positive = a > 0
    is_b_even = b % 2 == 0
    is_c_less_than_100 = c < 100
    
    return is_a_positive and is_b_even and is_c_less_than_100

if __name__ == '__main__':
    result = check_conditions(5, 4, 99)
    print(result)