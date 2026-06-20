def are_equivalent(statement1, statement2):
    a = True
    b = False
    result1 = eval(statement1)
    result2 = eval(statement2)
    return result1 == result2
if __name__ == '__main__':
    statement1 = 'a and not b'
    statement2 = '(not a) or (not b)'
    print(are_equivalent(statement1, statement2))