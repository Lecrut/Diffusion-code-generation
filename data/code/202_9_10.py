def find_maximum(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise ValueError('All inputs must be integers')
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value
if __name__ == '__main__':
    try:
        result = find_maximum(10, 20, 30)
        print(result)
    except ValueError as e:
        print(e)