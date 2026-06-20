def validate_statement(statement):
    return statement == "True" or statement == "False"

if __name__ == '__main__':
    print(validate_statement("True"))
    print(validate_statement("False"))
    print(validate_statement("123"))
    print(validate_statement("True "))
    print(validate_statement(" False"))