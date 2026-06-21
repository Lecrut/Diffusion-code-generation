def check_logical_opposition(statement1, statement2):
    negation_markers = {'not', 'no', 'never', 'none'}
    keywords = {'true', 'false'}

    def contains_negation(statement):
        return any(marker in statement.lower() for marker in negation_markers)

    def has_keyword(statement, keyword):
        return keyword.lower() in statement.lower()

    if contains_negation(statement1) and contains_negation(statement2):
        return False

    contradictions = {
        ('true', 'false'): True,
        ('false', 'true'): True,
        ('not true', 'false'): True,
        ('not false', 'true'): True,
        ('not not true', 'true'): True,
        ('not not false', 'false'): True
    }

    for keyword1, keyword2 in ((key, val) for key in keywords for val in keywords):
        if (has_keyword(statement1, keyword1) and has_keyword(statement2, keyword2)) or \
           (has_keyword(statement2, keyword1) and has_keyword(statement1, keyword2)):
            return contradictions.get((keyword1, keyword2), False)

    return False

if __name__ == '__main__':
    statement1 = "The sky is blue."
    statement2 = "The sky is not green."
    print(check_logical_opposition(statement1, statement2))