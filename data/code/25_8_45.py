def is_zero(value):

    def validate_input(val):
        if not isinstance(val, (int, float)):
            raise ValueError('Input must be an integer or float')
    try:
        validate_input(value)
        return value == 0
    except ValueError as e:
        print(e)
        return False
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(1))
    print(is_zero(-0.0))
    print(is_zero(0.0001))
    print(is_zero('0'))