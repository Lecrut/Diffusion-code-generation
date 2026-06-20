def logical_evaluator():
    statements = [
        "2 > 1",
        "3 < 5",
        "4 == 4",
        "1 != 0",
        "False or True"
    ]
    for statement in statements:
        yield eval(statement)

if __name__ == '__main__':
    for result in logical_evaluator():
        print(result)