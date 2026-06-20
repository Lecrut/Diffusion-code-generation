def logical_evaluator():
    yield True and False
    yield 1 == 1
    yield not (3 > 2)
    yield "hello" in "hello world"
    yield len([1, 2, 3]) == 3

if __name__ == '__main__':
    for result in logical_evaluator():
        print(result)