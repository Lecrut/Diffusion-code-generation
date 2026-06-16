def check_parity(value):
    if isinstance(value, (int, float)):
        try:
            int_value = int(value)
            return value > 0 and int_value % 2 != 0
        except ValueError:
            return False
    else:
        raise TypeError("Input must be an integer or float")
if __name__ == '__main__':
    print(check_parity(3))
    print(check_parity(-5))
    print(check_parity(4.7))
    print(check_parity(10))