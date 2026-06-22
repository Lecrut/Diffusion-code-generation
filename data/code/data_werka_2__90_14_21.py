def evaluate_or_condition(a, b):
    return a or b

if __name__ == '__main__':
    result = evaluate_or_condition(0, 1)
    print(result)
    result = evaluate_or_condition(None, "hello")
    print(result)
    result = evaluate_or_condition(False, True)
    print(result)
    result = evaluate_or_condition([], [1, 2])
    print(result)