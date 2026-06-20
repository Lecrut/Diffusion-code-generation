def evaluate_logical_expression():
    a = True
    b = False
    c = True

    result = (a and b) or (b and c)
    return result

if __name__ == '__main__':
    result = evaluate_logical_expression()
    print(result)