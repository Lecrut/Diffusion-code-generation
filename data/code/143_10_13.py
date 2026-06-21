def are_logically_contradictory(statement1, statement2):
    def evaluate_statement(statement, a, b):
        return eval(statement.replace('a', str(a)).replace('b', str(b)))

    truth_values = [(a, b) for a in [False, True] for b in [False, True]]
    
    for a, b in truth_values:
        if evaluate_statement(statement1, a, b) == evaluate_statement(statement2, a, b):
            return False
    return True

if __name__ == '__main__':
    statement1 = "a and not b"
    statement2 = "not a or b"
    print(are_logically_contradictory(statement1, statement2))