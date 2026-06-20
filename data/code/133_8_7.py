def logical_evaluator():
    statements = [
        (True and False),
        (False or True),
        not (True),
        (5 > 3) and (2 < 4),
        (10 == 10) or (1 != 1)
    ]
    for statement in statements:
        yield bool(statement)

if __name__ == '__main__':
    for result in logical_evaluator():
        print(result)