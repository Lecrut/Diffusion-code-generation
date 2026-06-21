def are_logically_contradictory(statement1, statement2):

    def evaluate_statement(statement, var_values):
        return eval(statement, {'__builtins__': None}, var_values)
    var_combinations = [(True, True), (True, False), (False, True), (False, False)]
    for vars in var_combinations:
        value1 = evaluate_statement(statement1, {'x': vars[0], 'y': vars[1]})
        value2 = evaluate_statement(statement2, {'x': vars[0], 'y': vars[1]})
        if value1 != value2:
            return True
    return False
if __name__ == '__main__':
    statement1 = 'x and y'
    statement2 = 'not x or not y'
    print(are_logically_contradictory(statement1, statement2))