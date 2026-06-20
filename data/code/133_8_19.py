def logical_generator():
    yield True
    yield False
    yield True

if __name__ == '__main__':
    gen = logical_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))