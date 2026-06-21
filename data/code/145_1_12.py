def nested_logical_operators():
    a = True
    b = False
    c = True

    result = not (a and (b or c)) and ((not a) or b)
    return result

if __name__ == '__main__':
    print(nested_logical_operators())