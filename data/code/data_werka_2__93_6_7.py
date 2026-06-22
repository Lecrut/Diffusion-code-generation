def check_both_false(a, b):
    truth_map = {True: 1, False: 0}
    return truth_map.get(bool(a), 0) + truth_map.get(bool(b), 0) == 0
if __name__ == '__main__':
    a = 0
    b = False
    result = check_both_false(a, b)
    print(result)