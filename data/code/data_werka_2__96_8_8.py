def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    result = evaluate_expression(True, False, True, False)
    print(result)