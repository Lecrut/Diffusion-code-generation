def validate_statement(statement):
    return eval(statement)

if __name__ == '__main__':
    print(validate_statement('True'))
    print(validate_statement('False'))
    print(validate_statement('2 + 2 == 4'))
    print(validate_statement('3 > 5'))