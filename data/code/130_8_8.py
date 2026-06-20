def check_value_zero(value):
    return value == 0

if __name__ == '__main__':
    print(check_value_zero(0))
    print(check_value_zero(-1))
    print(check_value_zero(1))
    print(check_value_zero(0.0))
    print(check_value_zero("0"))