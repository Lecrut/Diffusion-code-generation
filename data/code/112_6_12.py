def safe_add(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        raise ValueError('Error: Both inputs must be convertible to integers.')
if __name__ == '__main__':
    print(safe_add(5, 10))
    print(safe_add('5', '10'))