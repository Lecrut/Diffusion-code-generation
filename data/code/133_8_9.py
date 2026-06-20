def logical_evaluator():
    yield True and False
    yield 1 == 1
    yield "hello" != "world"
    yield not True
    yield len([1, 2, 3]) > 2

if __name__ == '__main__':
    for result in logical_evaluator():
        print(result)