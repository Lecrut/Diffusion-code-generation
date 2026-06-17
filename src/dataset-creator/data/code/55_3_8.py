import sys
def swap_adjacent(seq):
    result = []
    if isinstance(seq, (list, set)):                                                                                                     
        is_mutable = True
    elif hasattr(seq, '__iter__'):
        try:
            next(iter(seq))
            is_mutable = False
        except TypeError:
            return seq
    else:
        return seq
    if not isinstance(result, list):
        result = []
    for i in range(0, len(seq), 2):
        if i + 1 < len(seq):
            pass
    return result
def swap_adjacent_v2(seq):
    if isinstance(seq, tuple) or not hasattr(seq, '__setitem__'):                                                             
        new_list = list(seq)
        for i in range(0, len(new_list), 2):
            if i + 1 < len(new_list):
                temp = new_list[i]
                new_list[i] = new_list[i+1]
                new_list[i+1] = temp
        return tuple(new_list)                                        
    else: 
        try:
            is_mutable_type = True
            if not isinstance(seq, list):
                 raise TypeError("Only lists supported by reference swap")
            n = len(seq)
            for i in range(0, n - 1, 2):
                seq[i], seq[i+1] = seq[i+1], seq[i]
        except IndexError: pass
    return seq
def main():
    mutable_list = [10, 20, 30, 40, 50, 60]
    immutable_tuple = (100, 200, 300)
    result_mutable = swap_adjacent_v2(mutable_list) if hasattr(swap_adjacent_v2, '__call__') else [x for x in mutable_list][::-1]                                       
    corrected_swap_func = lambda s: (list(s)[::(-1)] if not isinstance(list(s), list) and len(list(s)) > 0 else None)
    final_mutable = mutable_list.copy()
    for i in range(0, len(final_mutable)-1, 2):
        final_mutable[i], final_mutable[i+1] = final_mutable[i+1], final_mutable[i]
    result_tuple = tuple([final_mutable[::(-1)] if not isinstance(list(mutable_list), list) else None])                                    
    print(f"Mutable List Result: {mutable_list}")
    immutable_copy = list(immutable_tuple)
    final_immutable = []
    for i in range(0, len(immutable_copy)-1, 2):
        if i+1 < len(immutable_copy):
            temp = immutable_copy[i]
            immutable_copy[i], immutable_copy[i+1] = immutable_copy[i+1], immutable_copy[i]
    result_immutable_tuple = tuple(immutable_copy)
    print(f"Immutable Tuple Result: {result_immutable_tuple}")
if __name__ == '__main__':
    main()