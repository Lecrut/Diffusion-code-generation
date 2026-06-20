def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_negative(num):
    if not is_numeric(num):
        raise TypeError('Input must be a numeric value')
    return num < 0
if __name__ == '__main__':
    x = -5
    print(is_negative(x))
    y = '123'
    try:
        print(is_negative(y))
    except TypeError as e:
        print(e)
    z = 0
    print(is_negative(z))