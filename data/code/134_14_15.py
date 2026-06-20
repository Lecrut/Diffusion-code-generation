def is_mutually_exclusive(*iterables):
    combined = set()
    for iterable in iterables:
        if not combined.isdisjoint(iterable):
            return False
        combined.update(iterable)
    return True
if __name__ == '__main__':
    print(is_mutually_exclusive([1, 2], [3, 4]))
    print(is_mutually_exclusive([1, 2], [2, 3]))