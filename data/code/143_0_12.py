def check_contradiction(statement1, statement2):
    return statement1 == 'not ' + statement2 or statement2 == 'not ' + statement1
if __name__ == '__main__':
    print(check_contradiction('the sky is blue', 'the sky is not blue'))
    print(check_contradiction('it is raining', 'it is not raining'))
    print(check_contradiction('I am happy', 'I am not happy'))
    print(check_contradiction('I am happy', 'I am sad'))