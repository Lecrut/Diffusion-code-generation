THRESHOLD = 0.8

def semantic_similarity(statement1, statement2):
    return abs(len(statement1) - len(statement2)) / max(len(statement1), len(statement2))

def are_mutually_exclusive(statement1, statement2):
    similarity = semantic_similarity(statement1, statement2)
    return similarity < THRESHOLD
if __name__ == '__main__':
    sample_statement1 = 'The sky is blue.'
    sample_statement2 = 'The grass is green.'
    result = are_mutually_exclusive(sample_statement1, sample_statement2)
    print(result)