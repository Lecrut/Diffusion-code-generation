def check_logical_opposition(statement1, statement2):
    negation_markers = {'not', 'no', 'never', 'none'}
    keywords = {'true', 'false'}

    def contains_negation(statement):
        return any(marker in statement.lower() for marker in negation_markers)

    if contains_negation(statement1) and contains_negation(statement2):
        return False

    for keyword in keywords:
        if (keyword.lower() in statement1.lower() and keyword.lower() not in statement2.lower()) or \
           (keyword.lower() not in statement1.lower() and keyword.lower() in statement2.lower()):
            return True

    return False

if __name__ == '__main__':
    statement1 = "The sky is blue."
    statement2 = "The sky is not green."
    print(check_logical_opposition(statement1, statement2))