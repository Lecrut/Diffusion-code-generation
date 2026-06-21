def check_nested_conditions():
    x = True
    y = False
    z = True
    result = x and (not y) or (z and y)
    return result
if __name__ == '__main__':
    print(check_nested_conditions())