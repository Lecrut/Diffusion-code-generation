def is_mutually_exclusive(*iterables):
    combined_set = set()
    for iterable in iterables:
        if not isinstance(iterable, (list, tuple, set)):
            raise ValueError("All inputs must be iterables")
        for item in iterable:
            if item in combined_set:
                return False
            combined_set.add(item)
    return True

if __name__ == '__main__':
    sample_iterables_1 = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
    result_1 = is_mutually_exclusive(*sample_iterables_1)
    print(f"Iterables: {sample_iterables_1}, Mutually Exclusive: {result_1}")

    sample_iterables_2 = ([1, 2, 3], [4, 5, 6], [7, 8, 9, 2])
    result_2 = is_mutually_exclusive(*sample_iterables_2)
    print(f"Iterables: {sample_iterables_2}, Mutually Exclusive: {result_2}")

    sample_iterables_3 = ([10, 20], [30, 40], [50, 60])
    result_3 = is_mutually_exclusive(*sample_iterables_3)
    print(f"Iterables: {sample_iterables_3}, Mutually Exclusive: {result_3}")