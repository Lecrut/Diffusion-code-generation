def check_contradiction(statement1, statement2):
    contradictions = {
        'The sky is blue': {'The sky is not blue'},
        'It will rain': {'It will not rain'},
        'I am happy': {'I am sad'},
        'She is here': {'She is not here'},
        'He is coming': {'He is not coming'}
    }
    
    return statement1 in contradictions and statement2 in contradictions[statement1]

if __name__ == '__main__':
    print(check_contradiction('The sky is blue', 'The sky is not blue'))
    print(check_contradiction('It will rain', 'It will not rain'))
    print(check_contradiction('I am happy', 'I am sad'))
    print(check_contradiction('She is here', 'She is not here'))
    print(check_contradiction('He is coming', 'He is not coming'))