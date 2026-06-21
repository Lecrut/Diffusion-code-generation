def greater_of_two(a, b):
    try:
        diff = a - b
        return a if diff // abs(diff) == 1 else b
    except TypeError:
        raise ValueError('Both inputs must be integers')

if __name__ == '__main__':
    x = 25
    y = 35
    result = greater_of_two(x, y)
    print(result)