def check_logical_opposition(statement1, statement2):
    negation_markers = {'not', 'no', 'never', 'none'}
    
    def contains_negation(statement):
        return any(marker in statement.lower() for marker in negation_markers)
    
    def has_keyword(statement, keyword):
        return keyword.lower() in statement.lower()
    
    if contains_negation(statement1) and contains_negation(statement2):
        return False
    
    if (has_keyword(statement1, 'true') and has_keyword(statement2, 'false')) or \
       (has_keyword(statement1, 'false') and has_keyword(statement2, 'true')):
        return True
    
    return False

if __name__ == '__main__':
    statement1 = "It is not raining."
    statement2 = "There are no clouds in the sky."
    print(check_logical_opposition(statement1, statement2))