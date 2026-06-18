import copy
def swap_adjacent(seq):
    if isinstance(seq, tuple) or (hasattr(seq, '__iter__') and not hasattr(seq, '_abc_impl')):
        try:
            list_seq = copy.copy(list(seq))
            for i in range(0, len(list_seq) - 1, 2):
                if i + 1 < len(list_seq):
                    list_seq[i], list_seq[i+1] = list_seq[i+1], list_seq[i]
            return tuple(list_seq) if isinstance(seq, tuple) else copy.copy(list_seq)
        except TypeError:
            raise ValueError("Input must be a sequence.")
    elif hasattr(seq, '__setitem__'):
        try:
            new_len = len(seq)
            for i in range(0, new_len - 1, 2):
                if i + 1 < new_len:
                    seq[i], seq[i+1] = seq[i+1], seq[i]
            return seq
        except (AttributeError, TypeError):
            raise ValueError("Input must be a mutable sequence.")
    else:
        new_seq = list(seq) if hasattr(seq, '__iter__') else [seq]
        for i in range(0, len(new_seq) - 1, 2):
            if i + 1 < len(new_seq):
                new_seq[i], new_seq[i+1] = new_seq[i+1], new_seq[i]
    return tuple(new_seq)
if __name__ == '__main__':
    data_list = [10, 20, 30, 40, 50]
    data_tuple = (10, 20, 30)
    print("Original List:", data_list)
    swapped_list_result = swap_adjacent(data_list)
    print("Swapped List Result:", swapped_list_result)
    print("\nOriginal Tuple:", data_tuple)
    swapped_tuple_result = swap_adjacent(data_tuple)
    print("Swapped Tuple Result:", swapped_tuple_result)
    print("\nVerification:")
    print("Is original list modified?", data_list == swapped_list_result)