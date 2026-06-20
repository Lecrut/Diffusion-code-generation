def logical_evaluator():
    statements = [
        True and False,
        not (True or False),
        5 > 3,
        2 == 2,
        "hello" != "world",
        len([1, 2, 3]) == 3
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
    print(next(evaluator))