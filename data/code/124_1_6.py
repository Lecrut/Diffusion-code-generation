def basic_arithmetic(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x // y
    return {'addition': add, 'subtraction': sub, 'multiplication': mul, 'floor_division': div}

if __name__ == '__main__':
    result = basic_arithmetic(15, 3)
    print(result)