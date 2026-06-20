def validate_and_evaluate(statement):
    if statement.lower() == 'true':
        return True
    elif statement.lower() == 'false':
        return False
    else:
        raise ValueError(f"Invalid statement encountered: '{statement}'")
if __name__ == '__main__':
    print(validate_and_evaluate('True'))
    print(validate_and_evaluate('False'))
    try:
        print(validate_and_evaluate('2 + 2 == 4'))
    except ValueError as e:
        print(e)