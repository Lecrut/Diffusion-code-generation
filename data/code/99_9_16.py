import operator

def evaluate_conditions(a, b, c):
    return (a and b) or not c

if __name__ == '__main__':
    result = evaluate_conditions(True, False, True)
    print(result)