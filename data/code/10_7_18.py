def yield_integers():
    for i in [1, 2, 3]:
        yield i

if __name__ == '__main__':
    gen = yield_integers()
    print(next(gen))