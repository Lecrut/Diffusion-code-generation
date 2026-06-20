def is_valid_boolean_expression(expression):
    try:
        eval(expression)
        return True
    except SyntaxError:
        return False

if __name__ == '__main__':
    print(is_valid_boolean_expression("True"))
    print(is_valid_boolean_expression("False"))
    print(is_valid_boolean_expression("1 == 1"))
    print(is_valid_boolean_expression("2 + 3"))