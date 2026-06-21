def check_logical_opposition(statement1: str, statement2: str) -> bool:
    keywords = {'and', 'or', 'not'}
    negation_markers = {'!', '~'}

    def contains_keyword_and_negation(statement):
        return any((keyword in statement for keyword in keywords)) and any((marker in statement for marker in negation_markers))
    if not (contains_keyword_and_negation(statement1) and contains_keyword_and_negation(statement2)):
        return False
    not_in_statement1 = 'not' not in statement1.lower()
    not_in_statement2 = 'not' not in statement2.lower()
    if (not_in_statement1 and 'or' in statement1) != (not_in_statement2 and 'or' in statement2):
        return True
    if (not_in_statement1 and 'and' in statement1) != (not_in_statement2 and 'and' in statement2):
        return True
    return False
if __name__ == '__main__':
    print(check_logical_opposition('The sky is blue or the grass is green', 'It is not the case that the sky is blue'))
    print(check_logical_opposition('The cat is on the mat and the dog is on the mat', 'The cat is on the mat or the dog is on the mat'))