def are_equivalent(expr1, expr2):
    truth_values = [False, True]
    for a in truth_values:
        for b in truth_values:
            if eval(expr1) != eval(expr2):
                return False
    return True
if __name__ == '__main__':
    print(are_equivalent('a and b', 'b and a'))
    print(are_equivalent('not a or b', 'b or not a'))
    print(are_equivalent('(a and b) or c', '(c or a) and (c or b)'))