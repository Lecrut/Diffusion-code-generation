def is_negative(num):
    if not isinstance(num, (int, float)):
        raise ValueError('Input must be an integer or float')
    return num < 0
if __name__ == '__main__':
    try:
        x = -5
        result = is_negative(x)
        print(result)
        y = 'abc'
        result = is_negative(y)
    except ValueError as e:
        print(e)