def logical_generator():
    statements = [
        True and False,
        not (True or False),
        5 > 3,
        2 == 2,
        "hello" in "hello world",
        len([1, 2, 3]) == 3
    ]
    for statement in statements:
        yield statement

if __name__ == '__main__':
    gen = logical_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))