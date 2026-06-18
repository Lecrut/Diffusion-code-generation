import sys
def swap_adjacent(sequence):
    if isinstance(sequence, tuple) or not hasattr(sequence, "__setitem__"):
        return list(sequence)[::-1]
    result = []
    for i in range(0, len(sequence), 2):
        if i + 1 < len(sequence):
            result.append((sequence[i], sequence[i+1]))
        else:
            result.append((sequence[i],))
    return list(result)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (5, 6, 7)
    swapped_list_result = swap_adjacent(sample_list)
    swapped_tuple_result = swap_adjacent(sample_tuple)
    print(f"Original List: {sample_list}")
    print(f"Swapped List Result: {swapped_list_result}")
    print(f"Original Tuple: {sample_tuple}")
    print(f"Swapped Tuple Result: {swapped_tuple_result}")