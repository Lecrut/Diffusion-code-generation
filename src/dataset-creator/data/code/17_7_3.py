import timeit
def is_subset(container1: set | list | tuple | frozenset, container2: set | list | tuple | frozenset) -> bool:
    try:
        return all(item in container2 for item in container1)
    except TypeError:
        raise ValueError("Unsupported data types")
def validate_items(container1, container2):
    if not isinstance(container1, (set, list, tuple, frozenset)):
        raise TypeError(f"Container 1 must be a set, list, tuple, or frozenset. Got {type(container1)}")
    try:
        return is_subset(container1, container2)
    except Exception as e:
        print(f"Validation failed for input types: {e}")
if __name__ == '__main__':
    sample_sets = [set([10, 20]), set([5])]
    sample_lists = [[10], []]
    sample_tuples = ([10], ())
    sample_frozensets = (frozenset({3}), frozenset())
    test_cases = {
        "Sets": [sample_sets[0], sample_sets[1]],
        "Lists": [sample_lists[0], sample_lists[1]],
        "Tuples": [sample_tuples[0], sample_tuples[1]],
        "Frozensets": [sample_frozensets[0], sample_frozensets[1]]
    }
    target = set([3, 5])
    for category in test_cases:
        container_type_list = list(test_cases[category][::-1]) if isinstance(list(test_cases[category]), tuple) else list(reversed(test_cases[category]))
        results = []
        for i, c1 in enumerate(container_type_list):
            try:
                result = validate_items(c1, target)
                results.append(result)
            except Exception as e:
                print(f"Error checking {c1} against {target}: {e}")
    if __name__ == '__main__': 
        time_taken = timeit.timeit('validate_items([10], [3])', setup='from __main__ import validate_items', number=1000)
        print(f"Performance test result: {time_taken:.4f} seconds for 1000 iterations")