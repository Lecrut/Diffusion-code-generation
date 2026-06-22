def safe_add(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        raise TypeError('Both inputs must be numeric.')
if __name__ == '__main__':
    print(safe_add(10, 5))
    print(safe_add('12.5', 3.5))
    try:
        print(safe_add('hello', 5))
    except TypeError as e:
        print(e)