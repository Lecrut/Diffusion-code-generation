def check_boolean_equality(x: bool, y: bool) -> bool:
    return x == y

if __name__ == '__main__':
    value_one = False
    value_two = False
    outcome = check_boolean_equality(value_one, value_two)
    print(outcome)