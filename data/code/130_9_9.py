def is_zero(value):
    try:
        return value == 0
    except TypeError:
        return False

if __name__ == '__main__':
    values = [1, 0, -1, '0', None]
    for val in values:
        print(f"{val} is zero: {is_zero(val)}")