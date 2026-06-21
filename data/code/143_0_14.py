def check_contradiction(statement1, statement2):
    if statement1 == statement2:
        return False
    if statement1.lower() == 'not ' + statement2.lower():
        return True
    if statement2.lower() == 'not ' + statement1.lower():
        return True
    return False
if __name__ == '__main__':
    print(check_contradiction('The sky is blue', 'The sky is not blue'))
    print(check_contradiction('The sky is blue', 'The sky is green'))
    print(check_contradiction('It is raining', 'It is not raining'))
    print(check_contradiction('It is raining', 'It is snowing'))