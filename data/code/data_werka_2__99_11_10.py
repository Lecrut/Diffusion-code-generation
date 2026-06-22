def evaluate_nested_conditions(a, b, c, d, e):
    return a and b or (c and d) or e
if __name__ == '__main__':
    result = evaluate_nested_conditions(True, False, True, True, False)
    print(result)