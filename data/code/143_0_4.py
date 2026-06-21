def check_contradiction(statement1, statement2):
    if statement1 == statement2:
        return False
    if 'not' in statement1 and statement1.replace('not', '') in statement2:
        return True
    if 'not' in statement2 and statement2.replace('not', '') in statement1:
        return True
    return False
if __name__ == '__main__':
    print(check_contradiction('The sky is blue.', 'The sky is not blue.'))
    print(check_contradiction('It is raining.', 'It is not raining.'))
    print(check_contradiction('The sun is shining.', 'The sun is not shining.'))
    print(check_contradiction('The moon is full.', 'The moon is not full.'))
    print(check_contradiction('The grass is green.', 'The grass is blue.'))
    print(check_contradiction('It is daytime.', 'It is nighttime.'))