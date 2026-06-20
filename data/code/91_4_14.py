def negate_boolean(value):
    return not value

if __name__ == '__main__':
    test_value = True
    result = negate_boolean(test_value)
    print(f"Negation of {test_value} is {result}")