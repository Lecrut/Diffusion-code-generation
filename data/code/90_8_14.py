def evaluate_or_condition(a, b):
    return (a > 5) or (b < 10)

if __name__ == '__main__':
    a_value = 6
    b_value = 9
    result = evaluate_or_condition(a_value, b_value)
    print(result)