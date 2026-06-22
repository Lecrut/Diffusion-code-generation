def generate_integers():
    VALUES = (7, 14, 21, 28, 35)
    for val in VALUES:
        yield val

if __name__ == '__main__':
    gen = generate_integers()
    result = next(gen)
    print(result)