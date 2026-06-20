def evaluate_complex_logic():
    x = (True and False) or (not True)
    y = (False and True) or (not False)
    z = not (x or y)
    w = (x and y) or (z and not y)
    return w

if __name__ == '__main__':
    result = evaluate_complex_logic()
    print(result)