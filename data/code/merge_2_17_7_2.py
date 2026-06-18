import timeit
def validate_presence(container1: set | list | tuple | frozenset, container2: set | list | tuple | frozenset) -> bool:
    try:
        return any(item in container2 for item in container1 if isinstance(item, (int, str))) or all(isinstance(x, (int, str)) and x in container2 for x in container1)
    except TypeError:
        return False
if __name__ == '__main__':
    sample_set = {1, 2, 'a', 'b'}
    sample_list = [3, 4, 'c']
    sample_tuple = (5, 'd')
    sample_frozenset = frozenset([6])
    test_cases = [
        ((sample_set, sample_list), True),
        ((sample_set, sample_frozenset), False),
        ((sample_list, sample_set), True),
        ((sample_tuple, sample_list), False)
    ]
    for (c1, c2), expected in test_cases:
        result = validate_presence(c1, c2)
        print(f"Input types ({type(c1).__name__}, {type(c2).__name__}): Expected={expected}, Got={result}")
    setup_code = "from __main__ import validate_presence; s=set([1,2]); l=[3]; t=(4); fs=frozenset()"
    time_result = timeit.timeit(stmt="validate_presence(s,l)", setup=setup_code, number=1000)
    print(f"Performance test (1000 iterations): {time_result:.6f} seconds")