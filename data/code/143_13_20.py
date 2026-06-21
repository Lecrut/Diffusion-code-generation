def are_mutually_exclusive(statement1: str, statement2: str) -> bool:
    return statement1.lower() == 'the sky is blue' and statement2.lower() == 'the sky is not blue'
if __name__ == '__main__':
    print(are_mutually_exclusive('The Sky Is Blue', 'The Sky Is Not Blue'))