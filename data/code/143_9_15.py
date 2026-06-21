def check_logical_opposition(statement1, statement2):
    keywords = ['not', 'and', 'or']
    negated_keywords = [f'not {keyword}' for keyword in keywords]
    
    def contains_keyword(statement, keyword):
        return keyword in statement.lower()
    
    def is_negated(statement, keyword):
        return f'not {keyword}' in statement.lower() or keyword in negated_keywords
    
    for keyword in keywords:
        if (contains_keyword(statement1, keyword) and not is_negated(statement2, keyword)) or \
           (contains_keyword(statement2, keyword) and not is_negated(statement1, keyword)):
            return True
    return False

if __name__ == '__main__':
    statement1 = "The sky is blue."
    statement2 = "It is not raining."
    print(check_logical_opposition(statement1, statement2))