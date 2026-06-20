def logical_evaluator():
    statements = [
        (True and False),
        (False or True),
        not (True and True),
        (5 > 3) == True,
        (2 < 1) != False
    ]
    for statement in statements:
        yield statement

if __name__ == '__main__':
    evaluator = logical_evaluator()
    print(next(evaluator))
    print(next(evaluator))
    print(next(evaluator))
    print(next(evaluator))
    print(next(evaluator))