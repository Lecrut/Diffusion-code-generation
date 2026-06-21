def generate_integers():
    yield 1
    yield 2
    yield 3

if __name__ == '__main__':
    gen = generate_integers()
    result = next(gen)
    print(result)