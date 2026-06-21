def check_contradiction(statement1, statement2):
    return statement1 != statement2
if __name__ == '__main__':
    print(check_contradiction('The sky is blue', 'The sky is green'))
    print(check_contradiction('It is raining', 'It is not raining'))
    print(check_contradiction('All men are mortal', 'Socrates is a man'))