def check_nested_conditions():
    a = True
    b = False
    c = True

    result = (a and (b or c)) or not (a and b)
    return result

if __name__ == '__main__':
    print(check_nested_conditions())