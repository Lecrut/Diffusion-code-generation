def are_logically_contradictory(statement1, statement2):
    truth_values = [(True, True), (True, False), (False, True), (False, False)]
    for v1, v2 in truth_values:
        if statement1(v1, v2) == statement2(v1, v2):
            return False
    return True
if __name__ == '__main__':

    def statement1(x, y):
        return x and (not y)

    def statement2(x, y):
        return not (x or y)
    print(are_logically_contradictory(statement1, statement2))