def is_zero(value):
    try:
        return value == 0
    except TypeError:
        return False
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(1))
    print(is_zero(0.0))
    print(is_zero('0'))
    print(is_zero(None))
    print(is_zero([0]))