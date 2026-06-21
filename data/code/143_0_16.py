def check_contradiction(statement1, statement2):
    if statement1 == statement2:
        return False
    if 'not' in statement1 and statement1.replace('not ', '') == statement2:
        return True
    if 'not' in statement2 and statement2.replace('not ', '') == statement1:
        return True
    return False
if __name__ == '__main__':
    print(check_contradiction('The sky is blue', 'The sky is not blue'))
    print(check_contradiction('The sky is blue', 'The sky is green'))
    print(check_contradiction('It will rain', 'It will not rain'))
    print(check_contradiction('It will rain', 'It might rain'))