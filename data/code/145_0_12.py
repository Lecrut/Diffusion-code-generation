def check_nested_conditions():
    a = True
    b = False
    c = True

    result = (a or b) and (c and not b)
    return result

if __name__ == '__main__':
    print(check_nested_conditions())