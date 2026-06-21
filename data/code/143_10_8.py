def are_logically_contradictory(statement1, statement2):
    truth_values = [(True, True), (True, False), (False, True), (False, False)]
    for val1, val2 in truth_values:
        if statement1(val1, val2) != statement2(val1, val2):
            return True
    return False

def sample_statement1(x, y):
    return x and (not y)

def sample_statement2(x, y):
    return not x or y
if __name__ == '__main__':
    print(are_logically_contradictory(sample_statement1, sample_statement2))