def is_numeric(value):
    return isinstance(value, (int, float))

def is_negative(num):
    if not is_numeric(num):
        raise TypeError('Input must be a numeric value')
    return num < 0
if __name__ == '__main__':
    x = -5
    print(is_negative(x))