def both_false(x, y):
    truth_table = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False
    }
    if (x, y) not in truth_table:
        raise ValueError("Inputs must be boolean values")
    return truth_table[(x, y)]

if __name__ == '__main__':
    x = False
    y = False
    print(both_false(x, y))