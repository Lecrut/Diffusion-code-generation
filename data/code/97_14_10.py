def compute_or_table():
    operands = [True, False]
    lookup = {
        (True, True): True,
        (True, False): True,
        (False, True): True,
        (False, False): False,
    }
    result = []
    for x in operands:
        for y in operands:
            result.append({"x": x, "y": y, "x | y": lookup[(x, y)]})
    return result

if __name__ == '__main__':
    print(compute_or_table())