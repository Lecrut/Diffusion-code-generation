def are_logically_contradictory(stmt1, stmt2):
    def evaluate(statement, a, b):
        return eval(statement.replace('a', str(a)).replace('b', str(b)))

    for a in [False, True]:
        for b in [False, True]:
            if evaluate(stmt1, a, b) == evaluate(stmt2, a, b):
                return False
    return True

if __name__ == '__main__':
    print(are_logically_contradictory('a and not b', 'b and not a'))