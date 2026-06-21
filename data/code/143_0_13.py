def check_contradiction(statement1, statement2):
    if statement1 == statement2:
        return False
    if 'not' in statement1.lower() and statement1[4:].lower() in statement2.lower():
        return True
    if statement1.lower() in statement2.lower() and 'not' in statement2.lower():
        return True
    return False
if __name__ == '__main__':
    print(check_contradiction('The sky is blue', 'The sky is not blue'))
    print(check_contradiction('The sky is blue', 'The sky is green'))
    print(check_contradiction('It will rain tomorrow', "It won't rain tomorrow"))
    print(check_contradiction('It will rain tomorrow', 'It might rain tomorrow'))