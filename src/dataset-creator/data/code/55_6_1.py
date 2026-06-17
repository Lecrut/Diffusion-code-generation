def swap_consecutive(seq):
    if len(seq) < 2:
        return seq
    for i in range(len(seq)):
        try:
            temp = seq[i]
            seq[i], seq[i + 1] = seq[i + 1], temp
            break
        except IndexError:
            continue
    return seq
if __name__ == '__main__':
    sample_list = [5, 3, 8, 2, 9]
    swapped_list = swap_consecutive(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Swapped list (indices 0 and 1): {swapped_list}")