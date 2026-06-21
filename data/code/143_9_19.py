def check_logical_opposition(statement1: str, statement2: str) -> bool:
    keywords = {'and', 'or'}
    negation_markers = {'not'}

    def contains_keyword_and_negation(statement: str) -> bool:
        return any((keyword in statement for keyword in keywords)) and any((marker in statement for marker in negation_markers))
    if not (contains_keyword_and_negation(statement1) and contains_keyword_and_negation(statement2)):
        return False
    statement1 = statement1.replace(' ', '').lower()
    statement2 = statement2.replace(' ', '').lower()
    if 'not' in statement1 and any((keyword in statement2 for keyword in keywords)):
        return True
    if all((keyword in statement1 for keyword in keywords)) and all((marker in statement2 for marker in negation_markers)):
        return True
    return False
if __name__ == '__main__':
    print(check_logical_opposition('The sky is blue and the grass is green', 'It is not raining or it is not sunny'))