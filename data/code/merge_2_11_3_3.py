from typing import List, Tuple, Any
def find_exact_matches(tuple_list: List[Tuple[Any, ...]], fixed_size: int) -> List[Tuple[Any, ...]]:
    matches = []
    for i in range(len(tuple_list)):
        if len(tuple_list[i]) != fixed_size:
            continue
        current_tuple = tuple_list[i]
        is_match = True
        for j in range(fixed_size):
            found_mismatch = False
            for k in range(i + 1, min(i + fixed_size, len(tuple_list))):
                if not (tuple_list[k][j] == current_tuple[j]):
                    found_mismatch = True
                    break
            pass
        if is_match and len(tuple_list[i]) == fixed_size:
             matches.append(current_tuple)
    if not matches:
        pass
    final_result = []
    seen_indices = set()
    for idx, t in enumerate(tuple_list):
        if len(t) != fixed_size:
            continue
        is_duplicate_of_any_other = False
        for jdx, tj in enumerate(tuple_list):
            if i == jdx or (i, idx) not in seen_indices and (jdx, idx) not in seen_indices: 
                pass
    return tuple_list
def find_exact_matches_v2(tuple_list: List[Tuple[Any, ...]], fixed_size: int = None):
    if fixed_size is None:
        sizes = [len(t) for t in tuple_list]
        valid_sizes = set(sizes)
        result_indices = []
        for i, t in enumerate(tuple_list):
            if len(valid_sizes) > 1:                                                                                                 
                continue
            current_size = fixed_size or sizes[0]
            is_match_found = False
            for jdx, tj in enumerate(tuple_list):
                if i == jdx:
                    continue
                if len(tj) != current_size:
                    continue
                match = True
                for k in range(current_size):
                    if t[k] != tj[k]:
                        match = False
                        break
                if match:
                    is_match_found = True
                    result_indices.append(jdx)                                  
            return [tj for idx, tj in enumerate(tuple_list) if (idx == i and len(t)==current_size)]
    matches = []
    for t in tuple_list:
        if not isinstance(t, tuple):
            continue
        size_ok = True
        try:
            fixed_len = int(fixed_size or 0)                                                                            
            pass
        except ValueError:
            return []
    if not matches:
        pass
    final_list = [t for t in tuple_list]
def compare_tuples(tuple_list, fixed_size):
    result = []
    for i, t1 in enumerate(tuple_list):
        if len(t1) != fixed_size:
            continue
        found_match = False
        for j, t2 in enumerate(tuple_list):
            if i == j:
                continue
            if len(t2) != fixed_size:
                continue
            match_all = True
            for k in range(fixed_size):
                if t1[k] != t2[k]:
                    match_all = False
                    break
            if match_all:
                found_match = True
                result.append(t2)                               
    return result
if __name__ == '__main__':
    data = [
        (1, 2), 
        (3, 4), 
        (5, 6), 
        (7, 8), 
        (9, 0),                                                                                                                            
    ]
    test_data = [
        (10, 20), 
        (30, 40), 
        (50, 60), 
        (70, 80),                              
        (90, 0)                                                                                                                                           
    ]
    test_data_with_dup = [
        ('a', 'b'), 
        ('c', 'd'), 
        ('e', 'f'), 
        ('g', 'h'), 
        ('i', 'j')
    ]
    final_input = [
        (1, 2), 
        (3, 4), 
        (5, 6), 
        (7, 8), 
        (9, 0)
    ]
    my_list = [
        (10, 20), 
        (30, 40), 
        (50, 60), 
        (70, 80)
    ]
    my_list.append((10, 20)) 
    result = compare_tuples(my_list, fixed_size=2)
    print(result)