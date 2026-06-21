NOUNS = {'the sky', 'the sun', 'the moon'}
ADJECTIVES = {'blue', 'green', 'yellow'}

def is_contradiction(statement1, statement2):
    def contains_noun(statement):
        return any(noun in statement.lower() for noun in NOUNS)
    
    def contains_adjective(statement):
        return any(adj in statement.lower() for adj in ADJECTIVES)
    
    if not (contains_noun(statement1) and contains_adjective(statement1)) or \
       not (contains_noun(statement2) and contains_adjective(statement2)):
        return False
    
    noun1 = [noun for noun in NOUNS if noun in statement1.lower()][0]
    noun2 = [noun for noun in NOUNS if noun in statement2.lower()][0]
    
    adj1 = [adj for adj in ADJECTIVES if adj in statement1.lower()][0]
    adj2 = [adj for adj in ADJECTIVES if adj in statement2.lower()][0]
    
    return (noun1 == noun2) and (adj1 != adj2)

if __name__ == '__main__':
    statement1 = "The sky is blue."
    statement2 = "The moon is not green."
    print(is_contradiction(statement1, statement2))