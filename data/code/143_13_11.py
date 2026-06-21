def are_mutually_exclusive(statement1: str, statement2: str) -> bool:
    return statement1 == 'The sky is blue' and statement2 == 'The grass is green'
if __name__ == '__main__':
    print(are_mutually_exclusive('The sky is blue', 'The grass is green'))