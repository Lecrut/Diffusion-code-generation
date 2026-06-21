def check_logical_opposition(statement1: str, statement2: str) -> bool:
    keywords = {'and', 'or', 'not'}
    negation_markers = {'!', '~'}

    def has_keyword(stmt):
        return any((keyword in stmt for keyword in keywords))

    def is_negated(stmt):
        return any((marker in stmt for marker in negation_markers))
    if not (has_keyword(statement1) and has_keyword(statement2)):
        return False
    if is_negated(statement1) != is_negated(statement2):
        return True
    return statement1.lower() == statement2.lower()
if __name__ == '__main__':
    print(check_logical_opposition('The sky is blue', 'The sky is not red'))
    print(check_logical_opposition('The sun rises in the east', 'The sun sets in the west'))