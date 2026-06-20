import operator

def compare_conditions(a, b, c):
    return (a and b) or c

if __name__ == '__main__':
    result = compare_conditions(True, False, True)
    print(result)