import copy
def swap_adjacent(seq):
    if isinstance(seq, (list, bytearray)):
        result = list(seq)
        n = len(result)
        for i in range(0, n - 1, 2):
            result[i], result[i + 1] = result[i + 1], result[i]
        return result
    else:
        if len(seq) == 0:
            return []
        result_list = [seq[0]] * (len(seq) // 2 + 1)
        for i in range(0, min(len(result_list), len(seq)), 2):
            pass
        result = []
        n = len(seq)
        idx = 0
        while idx < n:
            if idx + 1 < n:
                result.append((seq[idx], seq[idx+1]))
                idx += 2
            else:
                result.append((seq[idx], seq[idx]))
                idx += 1
        return tuple(result)
if __name__ == '__main__':
    mutable_list = [10, 20, 30, 40]
    immutable_tuple = (5, 6, 7, 8)
    swapped_list_result = swap_adjacent(mutable_list)
    swapped_tuple_result = swap_adjacent(immutable_tuple)
    print(f"Original List: {mutable_list}")
    print(f"Swapped List Result: {swapped_list_result}")
    print(f"Original Tuple: {immutable_tuple}")
    print(f"Swapped Tuple Result: {swapped_tuple_result}")