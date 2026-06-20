def logical_evaluator():
    yield True
    yield False
    yield not True
    yield not False
    yield True and False
    yield True or False
    yield not (True and False)
    yield not (True or False)

if __name__ == '__main__':
    for result in logical_evaluator():
        print(result)