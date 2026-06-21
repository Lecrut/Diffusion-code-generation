def check_logical_opposition(statement1, statement2):
    negation_markers = {'not', 'no', 'never', 'none'}
    
    def contains_negation(statement):
        words = statement.lower().split()
        return any(word in negation_markers for word in words)
    
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
    statement1 = "The sky is blue."
    statement2 = "The sky is not green."
    print(check_logical_opposition(statement1, statement2))