def is_mutually_exclusive(*iterables):
    seen = set()
    for iterable in iterables:
        if any((item in seen for item in iterable)):
            return False
        seen.update(iterable)
    return True
if __name__ == '__main__':
    print(is_mutually_exclusive([1, 2, 3], [4, 5, 6], [7, 8, 9]))
    print(is_mutually_exclusive([1, 2, 3], [3, 4, 5], [6, 7, 8]))