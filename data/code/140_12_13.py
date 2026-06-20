def validate_input(value):
    input_types = {'string': lambda x: isinstance(x, str) and bool(re.match('^[a-zA-Z0-9]+$', x)), 'integer': lambda x: isinstance(x, int) and x > 0}
    return any((input_types[key](value) for key in input_types))
if __name__ == '__main__':
    print(validate_input('Hello123'))
    print(validate_input(42))
    print(validate_input(''))
    print(validate_input('Hello!'))
    print(validate_input(-5))