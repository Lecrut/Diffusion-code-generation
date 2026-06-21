def check_nested_conditions():
    x = True
    y = False
    z = True

    result1 = (x and not y) or (z and y)
    return result1

if __name__ == '__main__':
    print(check_nested_conditions())