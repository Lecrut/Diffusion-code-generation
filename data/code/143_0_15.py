def check_contradiction(statement1, statement2):
    if statement1 == statement2:
        return False
    if 'not' in statement1 and statement1.replace('not ', '') in statement2.lower():
        return True
    if 'not' in statement2 and statement2.replace('not ', '') in statement1.lower():
        return True
    return False

if __name__ == '__main__':
    print(check_contradiction('The sky is blue', 'the sky is not blue'))
    print(check_contradiction('It will rain', 'it will not rain'))
    print(check_contradiction('I am happy', 'i am sad'))
    print(check_contradiction('He is coming', 'he is not coming'))