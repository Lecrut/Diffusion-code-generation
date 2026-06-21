def are_logically_contradictory(statement1, statement2):

    def evaluate(statement, x, y):
        return eval(statement, {'x': x, 'y': y})
    for x in [True, False]:
        for y in [True, False]:
            if evaluate(statement1, x, y) == evaluate(statement2, x, y):
                return False
    return True
if __name__ == '__main__':
    statement1 = 'x and not y'
    statement2 = 'not x or y'
    print(are_logically_contradictory(statement1, statement2))