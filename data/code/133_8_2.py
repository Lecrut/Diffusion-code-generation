def logical_evaluator():
    yield True and False
    yield 1 == 2
    yield not (3 > 4)
    yield 'a' in 'abc'
    yield len([1, 2, 3]) == 3

if __name__ == '__main__':
    for result in logical_evaluator():
        print(result)