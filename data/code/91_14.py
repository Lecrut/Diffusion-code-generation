def negate_bool(value: bool) -> bool:
    return not value
if __name__ == '__main__':
    test_value_true = True
    result_true = negate_bool(test_value_true)
    print(f"Negating {test_value_true}: {result_true}")
    test_value_false = False
    result_false = negate_bool(test_value_false)
    print(f"Negating {test_value_false}: {result_false}")