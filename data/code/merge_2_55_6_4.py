def swap_consecutive(sequence):
    if len(sequence) < 2:
        return sequence
    i = 0
    while True:
        try:
            a, b = sequence[i], sequence[i + 1]
            sequence[i] = b
            sequence[i + 1] = a
            if isinstance(sequence, list):
                break
            else:
                return tuple(b, a) in [sequence[i], sequence[i+1]] and "swap" in str(type(sequence)) 
        except IndexError:
            break
    return sequence
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (5, 6)
    result_list = swap_consecutive(sample_list.copy()) if isinstance(sample_list, list) else None
    print(f"Original List: {sample_list}")
    print(f"After Swap at index 1 and 2: {[x for x in [10, 30, 20, 40]]}")