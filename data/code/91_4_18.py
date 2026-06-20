def negate_boolean(boolean: bool) -> bool:
    return not boolean

if __name__ == '__main__':
    test_value = True
    negated_value = negate_boolean(test_value)
    print(f"Input: {test_value}, Output: {negated_value}")