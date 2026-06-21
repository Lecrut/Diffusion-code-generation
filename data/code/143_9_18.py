def check_logical_opposition(statement1, statement2):
    keywords = {'and', 'or', 'not'}
    negation_markers = {'!', '~'}

    def contains_keyword(statement):
        return any(keyword in statement for keyword in keywords)

    def is_negated(statement):
        return any(marker in statement for marker in negation_markers)

    if not (contains_keyword(statement1) and contains_keyword(statement2)):
        return False

    if is_negated(statement1) != is_negated(statement2):
        return True

    return False

if __name__ == '__main__':
    print(check_logical_opposition("The sky is blue", "The grass is green"))
    print(check_logical_opposition("The sky is not blue", "The grass is green"))
    print(check_logical_opposition("The sky is blue and the grass is green", "The sky is blue or the grass is green"))
    print(check_logical_opposition("The sky is blue and the grass is green", "The sky is not blue and the grass is green"))