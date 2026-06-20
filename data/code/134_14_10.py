def is_mutually_exclusive(*iterables):
    seen = set()
    for iterable in iterables:
        for item in iterable:
            if item in seen:
                return False
            seen.add(item)
    return True

if __name__ == '__main__':
    sample_iterables_1 = ([1, 2, 3], [4, 5, 6])
    print(f"Iterables: {sample_iterables_1}, Mutually Exclusive: {is_mutually_exclusive(*sample_iterables_1)}")
    
    sample_iterables_2 = ([1, 2, 3], [3, 4, 5])
    print(f"Iterables: {sample_iterables_2}, Mutually Exclusive: {is_mutually_exclusive(*sample_iterables_2)}")
    
    sample_iterables_3 = (['a', 'b'], ['c', 'd'])
    print(f"Iterables: {sample_iterables_3}, Mutually Exclusive: {is_mutually_exclusive(*sample_iterables_3)}")