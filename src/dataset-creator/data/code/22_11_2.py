def remove_at_index(sequence, index):
    if not isinstance(index, int) or index < 0:
        raise ValueError("Index must be a non-negative integer.")
    return sequence[:index] + sequence[index+1:]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_remove = 2
    result = remove_at_index(sample_list, index_to_remove)
    print(result)