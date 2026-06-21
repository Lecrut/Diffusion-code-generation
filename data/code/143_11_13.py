def check_contradictions(expr1, expr2):
    truth_table = {}
    for i in range(2**len(expr1)):
        inputs = [bool(i & (1 << j)) for j in range(len(expr1))]
        result1 = eval(expr1, {'__builtins__': None}, dict(zip(expr1, inputs)))
        result2 = eval(expr2, {'__builtins__': None}, dict(zip(expr2, inputs)))
        truth_table[inputs] = (result1, result2)
    return any(result1 == result2 for result1, result2 in truth_table.values())

if __name__ == '__main__':
    expr1 = "a and not b"
    expr2 = "not a or b"
    print(check_contradictions(expr1, expr2))