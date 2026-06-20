def evaluate_or_condition(a, b):
    return (a > 5) or (b < 10)

if __name__ == '__main__':
    a = 3
    b = 9
    result = evaluate_or_condition(a, b)
    print(result)