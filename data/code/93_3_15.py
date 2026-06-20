def is_false(value):
    return not value

if __name__ == '__main__':
    x = False
    y = False
    result = is_false(x) and is_false(y)
    print(result)