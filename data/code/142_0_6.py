def evaluate_boolean_equality(x: bool, y: bool) -> bool:
    return x == y

if __name__ == '__main__':
    value1 = True
    value2 = False
    outcome = evaluate_boolean_equality(value1, value2)
    print(outcome)