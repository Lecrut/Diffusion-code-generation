import operator

def compare_conditions(a, b, c, d):
    return (a and b) or (c and d)

if __name__ == '__main__':
    print(compare_conditions(True, False, True, False))
    print(compare_conditions(False, True, False, True))
    print(compare_conditions(True, True, False, False))
    print(compare_conditions(False, False, True, True))