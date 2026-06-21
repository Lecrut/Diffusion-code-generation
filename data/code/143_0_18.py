def check_contradiction(statement1, statement2):
    if statement1 == statement2:
        return False
    if 'not' in statement1 and statement1.replace('not', '').strip() in statement2:
        return True
    if 'not' in statement2 and statement2.replace('not', '').strip() in statement1:
        return True
    return False
if __name__ == '__main__':
    print(check_contradiction('The sky is blue.', 'The sky is not green.'))
    print(check_contradiction('I am happy.', 'I am sad.'))
    print(check_contradiction('It will rain.', 'It will not rain.'))
    print(check_contradiction('She is a teacher.', 'She is a doctor.'))
    print(check_contradiction('The world is flat.', 'The world is round.'))