import operator

def compare_conditions(a, b):
    return a and (not b)
if __name__ == '__main__':
    result = compare_conditions(True, False)
    print(result)