def phrase_generator(limit=None):
    phrase = 'Repeat an action many times now'
    count = 0
    if limit is not None:
        while count < limit:
            yield phrase
            count += 1
    else:
        while True:
            yield phrase
if __name__ == '__main__':
    print("Testing with no limit (indefinite):")
    generator_infinite = phrase_generator()
    for i in range(5):
        print(next(generator_infinite))
    print("\nTesting with a limit of 3:")
    generator_limited = phrase_generator(limit=3)
    for i in range(3):
        print(next(generator_limited))