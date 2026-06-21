def nested_logical_operators():
    a = True
    b = False
    c = True

    result = (a and b) or (c and not b)
    return result

if __name__ == '__main__':
    print(nested_logical_operators())