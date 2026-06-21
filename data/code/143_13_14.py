def are_mutually_exclusive(statement1, statement2):
    return statement1 == 'I am a cat' and statement2 == 'I am a dog'
if __name__ == '__main__':
    print(are_mutually_exclusive('I am a cat', 'I am a dog'))