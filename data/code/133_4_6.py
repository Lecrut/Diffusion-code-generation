def validate_statement(statement):
    if statement.lower() == 'true':
        return True
    elif statement.lower() == 'false':
        return False
    else:
        raise ValueError(f"Invalid value encountered: '{statement}'")

if __name__ == '__main__':
    print(validate_statement('True'))
    print(validate_statement('False'))
    try:
        print(validate_statement('2 + 2 == 4'))
    except ValueError as e:
        print(e)