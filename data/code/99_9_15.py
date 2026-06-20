import operator

def compare_conditions(a, b, c):
    return (a or b) and (not c)
if __name__ == '__main__':
    print(compare_conditions(True, False, True))
    print(compare_conditions(False, True, False))