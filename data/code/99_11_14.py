def evaluate_nested_conditions(a, b, c, d, e, f, g, h):
    return a and b or (c and d) or (e and f) or (g and h)
if __name__ == '__main__':
    result = evaluate_nested_conditions(True, False, True, True, False, False, True, False)
    print(result)