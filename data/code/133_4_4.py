def validate_statement(statement):
    return statement.lower() == 'true'

if __name__ == '__main__':
    print(validate_statement('True'))
    print(validate_statement('false'))
    print(validate_statement('TRUE'))
    print(validate_statement('FALSE'))
    print(validate_statement('not a boolean'))