def are_mutually_exclusive(statement1: str, statement2: str) -> bool:
    return statement1 != statement2
if __name__ == '__main__':
    print(are_mutually_exclusive('The sky is blue.', 'The sky is green.'))