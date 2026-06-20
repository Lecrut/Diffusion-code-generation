def has_common_elements(iterables):
    combined_set = set()
    for iterable in iterables:
        if not isinstance(iterable, (list, tuple, set)):
            raise TypeError("All elements must be iterable")
        combined_set.update(iterable)
    return len(combined_set) < sum(len(it) for it in iterables)

def is_mutually_exclusive(*iterables):
    return not has_common_elements(iterables)

if __name__ == '__main__':
    sample_iterables_1 = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
    print(f"Iterables: {sample_iterables_1}, Mutually Exclusive: {is_mutually_exclusive(*sample_iterables_1)}")
    
    sample_iterables_2 = ([1, 2, 3], [4, 5, 6], [7, 8, 9, 1])
    print(f"Iterables: {sample_iterables_2}, Mutually Exclusive: {is_mutually_exclusive(*sample_iterables_2)}")
    
    sample_iterables_3 = ([10, 11], [12, 13], [14, 15])
    print(f"Iterables: {sample_iterables_3}, Mutually Exclusive: {is_mutually_exclusive(*sample_iterables_3)}")