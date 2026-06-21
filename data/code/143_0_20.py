def check_contradiction(statement1, statement2):
    if statement1 == statement2:
        return False
    if 'not' in statement1 and statement2.replace(' ', '').lower() == statement1.replace('not', '', 1).replace(' ', '').lower():
        return True
    if statement1.replace(' ', '').lower() == statement2.replace(' ', '').lower():
        return True
    return False
if __name__ == '__main__':
    print(check_contradiction('The sky is blue.', 'The sky is not blue.'))
    print(check_contradiction('The sky is blue.', 'The sky is green.'))
    print(check_contradiction('It will rain.', 'It will not rain.'))
    print(check_contradiction('It will rain.', 'It might rain.'))