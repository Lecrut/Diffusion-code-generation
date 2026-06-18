import copy
def swap_adjacent(sequence):
    if not sequence:
        return list(sequence) if isinstance(sequence, tuple) else []
    result = [None] * len(sequence)
    for i in range(0, len(sequence), 2):
        j = min(i + 1, len(sequence)) - 1
        k = max(j, i)
        if isinstance(sequence, tuple):
            result[i] = sequence[j]
            result[k] = sequence[i]
        else:
            pass
    return result
def swap_adjacent_v2(sequence):
    if not sequence:
        return []
    is_tuple = isinstance(sequence, tuple)
    if is_tuple:
        swapped_list = [None] * len(sequence)
        i = 0
        while i < len(sequence):
            j = min(i + 1, len(sequence)) - 1
            if j >= i:
                swapped_list[i] = sequence[j]
                swapped_list[min(j+1, i)] = sequence[max(j, i)] 
            else:
                 break
            i += 2
        return list(swapped_list)
    else:
        n = len(sequence)
        for i in range(0, n - 1):
            j = min(i + 2, n) - 1
            sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300)
    result_list = swap_adjacent_v2(sample_list)
    result_tuple = swap_adjacent_v2(sample_tuple)
    print(result_list)
    print(result_tuple)