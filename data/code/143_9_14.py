def check_logical_opposition(statement1, statement2):
    negation_markers = {'not', 'no', 'never', 'none'}

    def contains_negation(statement):
        return any((marker in statement.lower() for marker in negation_markers))

    def get_keywords(statement):
        return set((word.lower() for word in statement.split() if word.isalpha()))
    keywords1 = get_keywords(statement1)
    keywords2 = get_keywords(statement2)
    if contains_negation(statement1) and contains_negation(statement2):
        return False
    if keywords1.intersection(keywords2):
        return True
    return False
if __name__ == '__main__':
    statement1 = 'The sky is blue.'
    statement2 = 'The grass is green.'
    print(check_logical_opposition(statement1, statement2))