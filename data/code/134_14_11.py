def is_mutually_exclusive(*iterables):
    combined_set = set()
    for iterable in iterables:
        if combined_set.intersection(iterable):
            return False
        combined_set.update(iterable)
    return True
if __name__ == '__main__':
    sample1 = [1, 2, 3]
    sample2 = [4, 5, 6]
    sample3 = [7, 8, 9]
    print(is_mutually_exclusive(sample1, sample2, sample3))
    sample4 = [1, 2, 3]
    sample5 = [3, 4, 5]
    print(is_mutually_exclusive(sample4, sample5))