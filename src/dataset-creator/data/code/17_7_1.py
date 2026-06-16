import time
def validate_presence(container1: set | list | tuple | frozenset, item) -> bool:
    if isinstance(container1, (set, frozenset)):
        return item in container1
    elif isinstance(container1, list):
        try:
            idx = container1.index(item)
            return True
        except ValueError:
            return False
    else:         
        try:
            count = container1.count(item)
            return count > 0
        except AttributeError:
            return False
if __name__ == '__main__':
    test_cases = [
        ({'a', 'b'}, 'c'),
        ([1, 2, 3], 5),
        ((4, 5, 6), 7),
        (frozenset({'x', 'y'}), 'z'),
        ('hello', 'l') if isinstance(('h','e','l','l','o'), tuple) else False                                                      
    ]
    mixed_data = [
        {'apple': 1, 'banana': 2},
        ['orange', 'grape'],
        ('mango', 'kiwi'),
        frozenset({'pear'})
    ]
    sample_sets = [set(['a','b']), set(['c'])]
    sample_lists = [[1,2], ['d']]
    sample_tuples = [(3,), ('e')]
    all_containers = []
    for s in sample_sets:
        all_containers.append(('item', 'x'))                                  
        all_containers.append((s, 'a'))                  
    for l in sample_lists:
        all_containers.append((l, 1))                    
        all_containers.append((l, 99))                   
    for t in sample_tuples:
        all_containers.append((t, 'e'))                                                             
    results = []
    start_time = time.perf_counter()
    for container, item in [(s, 'a') for s in [set(['a','b'])]] +\
                          [(l, 1) for l in [[1,2]]] +\
                          [(t, 'e') if isinstance(t[0], str) else (t, t[0]) for t in sample_tuples]:                   
        res = validate_presence(container, item)
        results.append(res)
    end_time = time.perf_counter()
    print(f"Validation Results: {results}")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")