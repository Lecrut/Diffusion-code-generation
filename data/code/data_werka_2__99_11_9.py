def evaluate_nested_conditions(a, b, c, d):
    return a and b or c and d

if __name__ == '__main__':
    result = evaluate_nested_conditions(True, False, True, True)
    print(result)