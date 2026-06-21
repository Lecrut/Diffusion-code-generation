def check_logical_opposition(statement1, statement2):
    negation_markers = {'not', 'no', 'never', 'none'}
    def contains_negation(statement):
        return any(marker in statement.lower() for marker in negation_markers)
    
    def has_keyword(statement, keyword):
        return keyword.lower() in statement.lower()
    
    if contains_negation(statement1) and contains_negation(statement2):
        return False
    
    keywords = {'true', 'false'}
    for keyword in keywords:
        if (has_keyword(statement1, keyword) and not has_keyword(statement2, keyword)) or \
           (not has_keyword(statement1, keyword) and has_keyword(statement2, keyword)):
            return True
    
    return False

if __name__ == '__main__':
    statement1 = "It is raining."
    statement2 = "It is not sunny."
    print(check_logical_opposition(statement1, statement2))