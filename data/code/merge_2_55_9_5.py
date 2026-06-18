def swap_adjacent(seq):
    if not seq:
        return []
    result = list(seq)
    for i in range(0, len(result), 2):
        if i + 1 < len(result):
            result[i], result[i+1] = result[i+1], result[i]
    return result
if __name__ == '__main__':
    sample_data = [5, 3, 8, 1, 'a', 'b']
    swapped_result = swap_adjacent(sample_data)
    print(swapped_result)