def phrase_generator(limit=None):
    phrase = 'Repeat an action many times now'
    count = 0
    while True:
        yield phrase
        if limit is not None and count >= limit:
            break
        count += 1
if __name__ == '__main__':
    print("Testing without limit:")
    generator1 = phrase_generator()
    for i in range(5):
        print(next(generator1))
    print("\nTesting with limit of 3:")
    generator2 = phrase_generator(limit=3)
    for i in range(5):
        try:
            print(next(generator2))
        except StopIteration:
            break