def check_logical_opposition(statement1, statement2):
    negation_markers = {'not', 'no', 'never', 'none'}
    keywords1 = set(statement1.lower().split())
    keywords2 = set(statement2.lower().split())

    if any(keyword in negation_markers for keyword in keywords1) and any(keyword in negation_markers for keyword in keywords2):
        return False
    elif not (keywords1 & negation_markers) and not (keywords2 & negation_markers):
        return False
    else:
        return True

if __name__ == '__main__':
    statement1 = "The sky is blue."
    statement2 = "The sky is not green."
    print(check_logical_opposition(statement1, statement2))