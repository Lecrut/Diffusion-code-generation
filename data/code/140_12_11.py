class InputValidator:

    def is_valid(self, value):
        if isinstance(value, str) and value:
            return bool(re.match('^[a-zA-Z0-9]+$', value))
        elif isinstance(value, int) and value > 0:
            return True
        return False
if __name__ == '__main__':
    validator = InputValidator()
    print(validator.is_valid('Hello123'))
    print(validator.is_valid(42))
    print(validator.is_valid(''))
    print(validator.is_valid('Hello!'))
    print(validator.is_valid(-5))