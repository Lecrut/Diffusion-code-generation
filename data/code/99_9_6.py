import operator

def compare_conditions(a, b, c):
    return a and b or c
if __name__ == '__main__':
    print(compare_conditions(True, False, True))
    print(compare_conditions(False, False, False))