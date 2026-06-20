def is_mutually_exclusive(*iterables):
    seen = set()
    for iterable in iterables:
        if any((item in seen for item in iterable)):
            return False
        seen.update(iterable)
    return True
if __name__ == '__main__':
    sample1 = [1, 2, 3]
    sample2 = [4, 5, 6]
    sample3 = [7, 8, 9]
    print(f'Sample 1 and 2: {is_mutually_exclusive(sample1, sample2)}')
    print(f'Sample 1 and 3: {is_mutually_exclusive(sample1, sample3)}')
    print(f'Sample 2 and 3: {is_mutually_exclusive(sample2, sample3)}')
    print(f'All together: {is_mutually_exclusive(sample1, sample2, sample3)}')