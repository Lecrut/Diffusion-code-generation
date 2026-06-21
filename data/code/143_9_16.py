def check_logical_opposition(statement1, statement2):
    negation_markers = {'not', 'no', 'never', 'cannot'}
    keywords = {'statement1': set(), 'statement2': set()}
    
    for word in statement1.split():
        if word.lower() in negation_markers:
            keywords['statement1'].add('negated')
        else:
            keywords['statement1'].add(word.lower())
    
    for word in statement2.split():
        if word.lower() in negation_markers:
            keywords['statement2'].add('negated')
        else:
            keywords['statement2'].add(word.lower())
    
    return not (keywords['statement1'] & keywords['statement2'])

if __name__ == '__main__':
    print(check_logical_opposition("The sky is blue", "The sky is not green"))
    print(check_logical_opposition("I cannot eat", "I can eat"))