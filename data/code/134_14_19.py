def is_mutually_exclusive(*iterables):
    combined_set = set()
    for iterable in iterables:
        if not isinstance(iterable, (list, tuple, set)):
            raise ValueError('All inputs must be iterable')
        combined_set.update(iterable)
    return len(combined_set) == sum((len(x) for x in iterables))
if __name__ == '__main__':
    print(is_mutually_exclusive([1, 2], [3, 4]))
    print(is_mutually_exclusive([1, 2], [2, 3]))
    print(is_mutually_exclusive('abc', 'def'))
    print(is_mutually_exclusive('abc', 'acb'))