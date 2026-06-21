def check_contradiction(statement1, statement2):
    return statement1 == 'not ' + statement2 or statement2 == 'not ' + statement1
if __name__ == '__main__':
    print(check_contradiction('The sky is blue', 'The sky is not blue'))
    print(check_contradiction('It is raining', 'It is not raining'))
    print(check_contradiction('I am happy', 'I am sad'))
    print(check_contradiction('She is here', 'She is not here'))
    print(check_contradiction('He is coming', 'He is not coming'))