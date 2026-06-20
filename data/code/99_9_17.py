import operator

def compare_conditions(a, b, c):
    return (operator.and_(a, b)) or c

if __name__ == '__main__':
    print(compare_conditions(True, False, True))
    print(compare_conditions(False, True, False))
    print(compare_conditions(True, True, False))
    print(compare_conditions(False, False, True))