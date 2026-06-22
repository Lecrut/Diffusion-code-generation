TRUE_VALUE = 1
FALSE_VALUE = 0

def toggle_bools(values):
    mapping = {TRUE_VALUE: FALSE_VALUE, FALSE_VALUE: TRUE_VALUE}
    result = []
    for val in values:
        if val:
            result.append(FALSE_VALUE)
        else:
            result.append(TRUE_VALUE)
    return [bool(x) for x in result]

if __name__ == '__main__':
    data = [True, False, True, False]
    output = toggle_bools(data)
    print(output)