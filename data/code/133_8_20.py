def logical_evaluator():
    yield True
    yield False
    yield True
    yield not True
    yield not False

if __name__ == '__main__':
    for result in logical_evaluator():
        print(result)