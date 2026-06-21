def is_not_statement(statement):
    return statement.startswith('not ')

def remove_not(statement):
    if is_not_statement(statement):
        return statement[4:]
    return statement

def check_contradiction(statement1, statement2):
    if statement1 == statement2:
        return False
    cleaned_statement1 = remove_not(statement1)
    cleaned_statement2 = remove_not(statement2)
    return (is_not_statement(statement1) != is_not_statement(statement2)) and (cleaned_statement1 == cleaned_statement2)

if __name__ == '__main__':
    print(check_contradiction('The sky is blue', 'The sky is not blue'))
    print(check_contradiction('The sky is blue', 'The sky is green'))
    print(check_contradiction('It will rain', 'It will not rain'))
    print(check_contradiction('It will rain', 'It might rain'))