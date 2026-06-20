def evaluate_boolean_generator():
    yield True
    yield False
    yield not True
    yield not False

if __name__ == '__main__':
    gen = evaluate_boolean_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))