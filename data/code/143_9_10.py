def check_logical_opposition(statement1, statement2):
    keywords = {'and', 'or', 'not'}
    negation_markers = {'!', '~'}

    def contains_keyword_or_negation(statement):
        return any((keyword in statement for keyword in keywords)) or any((marker in statement for marker in negation_markers))
    if not (contains_keyword_or_negation(statement1) and contains_keyword_or_negation(statement2)):
        return False
    if 'not' in statement1 and 'not' in statement2:
        return False
    if 'not' in statement1 and 'not' not in statement2 or ('not' not in statement1 and 'not' in statement2):
        return True
if __name__ == '__main__':
    print(check_logical_opposition('The sky is blue.', 'The sky is not blue.'))
    print(check_logical_opposition('The sky is blue.', 'The sky is green.'))